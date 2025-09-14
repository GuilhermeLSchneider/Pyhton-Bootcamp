import os
import torch
import torch.nn as nn
from torch.nn import functional as F

# hyperparameters
batch_size = 32 # how many independent sequences will we process in parallel?
block_size = 8 # what is the maximum context length for predictions?
max_iters = 3000
eval_interval = 300
learning_rate = 1e-2
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
# ------------
print(device)
torch.manual_seed(1337)

# wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(file, 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
# Criando um mapeamento de caracteres para inteiros e vice-versa
stoi = { ch:i for i,ch in enumerate(chars) } # palavra para índice
itos = { i:ch for i,ch in enumerate(chars) } # índice para palavra
encode = lambda s: [stoi[c] for c in s] # conversão de caracteres para lista de índices
decode = lambda l: ''.join([itos[i] for i in l]) # conversão de lista de índices para caracteres

data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9*len(data))
train_data = data[:n]
val_data = data[n:]

def get_batch(split):
    data = train_data if split == 'train' else val_data # separa os dados de treino e validação
    ix = torch.randint(len(data) - block_size, (batch_size,)) # índices aleatórios para o batch
    x = torch.stack([data[i:i+block_size] for i in ix]) # inputs
    y = torch.stack([data[i+1:i+block_size+1] for i in ix]) # targets
    x, y = x.to(device), y.to(device)
    return x, y

@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

# super simple bigram model
class BigramLanguageModel(nn.Module):

    def __init__(self, vocab_size):
        super().__init__()
        # Tabela de embedding: cada token é mapeado diretamente para os logits dos próximos tokens
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(self, idx, targets=None):
        # idx e targets são tensores (B,T) de inteiros
        logits = self.token_embedding_table(idx) # (B,T,C), onde C = vocab_size

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)   # reshape para (B*T, C) - importante converter para 2D antes de aplicar cross-entropy
            targets = targets.view(B*T)    # reshape para (B*T) - converter pra 1D por questão da loss
            loss = F.cross_entropy(logits, targets) # calcula a perda

        return logits, loss

    def generate(self, idx, max_new_tokens):
        # Gera novos tokens a partir de um contexto inicial idx
        for _ in range(max_new_tokens):
            logits, loss = self(idx)
            logits = logits[:, -1, :] # pega apenas o último passo de tempo
            probs = F.softmax(logits, dim=-1) # converte logits em probabilidades
            idx_next = torch.multinomial(probs, num_samples=1) # amostra o próximo token
            idx = torch.cat((idx, idx_next), dim=1) # adiciona o novo token à sequência
        return idx
        # importante notar que o modelo leva em conta apenas o último token para prever o próximo, não o contexto completo ainda

model = BigramLanguageModel(vocab_size)
m = model.to(device)

optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

for iter in range(max_iters):

    # every once in a while evaluate the loss on train and val sets
    if iter % eval_interval == 0:
        losses = estimate_loss()
        print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

    # sample a batch of data
    xb, yb = get_batch('train')

    # evaluate the loss
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

context = torch.zeros((1, 1), dtype=torch.long, device=device)
print(decode(m.generate(context, max_new_tokens=500)[0].tolist()))
