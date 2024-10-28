import numpy as np
import pandas as pd

data = {'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB', "WP", "WP"],
        'Nome': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah', 'John', 'David'],
        'Venda': [200, 120, 340, 124, 243, 350, 600, 494]}

df = pd.DataFrame(data)
print(df)

# print(df.groupby('Empresa').sum())
# print(df.groupby('Empresa').describe())
# print(df.groupby('Empresa').count())

group_nome = df.groupby('Nome')
print(group_nome.sum())