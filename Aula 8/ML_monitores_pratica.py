from bs4 import BeautifulSoup
import requests

# Utilização de uma input para filtrar os monitores de acordo com a marca inserida
print('Insira a marca do monitor que você deseja pesquisar: ')
monitor_brand = input('>')
print(f'Filtrando monitores da marca: {monitor_brand}')

def find_monitor():
    # Seção do acesso, processamento do HTML, e filtragem dos monitores
    html_text = requests.get('https://lista.mercadolivre.com.br/informatica/monitores-acessorios/monitores/monitor-180hz_CustoFrete_Gratis_NoIndex_True#applied_filter_id%3Dshipping_cost_highlighted_free%26applied_filter_name%3DCusto+do+frete%26applied_filter_order%3D2%26applied_value_id%3Dfree%26applied_value_name%3DGr%C3%A1tis%26applied_value_order%3D1%26applied_value_results%3D158%26is_custom%3Dfalse').text
    soup = BeautifulSoup(html_text, 'lxml')
    monitor = soup.find_all('li', class_='ui-search-layout__item')

    # Iteração para pegar as informações de cada monitor, e salvar em um arquivo .txt
    for index, item in enumerate(monitor):
        # Pega o nome, preço, parcelamento, e link do produto
        product_name = item.find('a', class_='').text
        product_price = item.find('span', class_='andes-money-amount__fraction').text
        installment_section = item.find('span', class_='poly-price__installments poly-text-primary')
        # Verificação se o parcelamento está disponível
        # O site escolhido possui as informações em spans diferentes, necessitando de um tratamento diferente
        if installment_section:
            installments = installment_section.text.split('em')[1].strip() if 'em' in installment_section.text else installment_section.text.strip()
        else:
            installments = 'Parcelamento indisponível'
        
        more_info = item.h2.a['href']
        
        # if monitor_brand in product_name:
        #     print(f'Nome do Produto: {product_name.strip()}')
        #     print(f'Preço: R${product_price.strip()}')
        #     print(f'Parcelamento: {installments}')
        #     print(f'Mais Informações: {more_info}')
        #     print('===============================')
        
        # Verificação se o nome do produto contém a marca inserida, caso contenha, salva o arquivo
        if monitor_brand in product_name:
            with open(f'Aula 8/monitores/{index}.txt', 'w') as f:
                f.write(f'Nome do Produto: {product_name.strip()} \n')
                f.write(f'Preço: {product_price.strip()} \n')
                f.write(f'Parcelamento: {installments} \n')
                f.write(f'Mais Informações: {more_info}')
                print('===============================')
            print(f'Arquivo salvo: {index}')

if __name__ == '__main__':
    find_monitor() # Chamada da função para filtrar os monitores
