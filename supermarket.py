# %%
# Importando bibliotecas necessárias
import pandas as pd

# Realizando a leitura do arquivo
df = pd.read_csv('Superstore.csv', encoding='windows-1252')
df

# %%
# Verificando a estrutura dos dados
print(df.info())

# %%
# Fazendo uma descrição/resumo dos dados
print(df.describe())

# %%
# Verifica valores ausentes
print(df.isnull().sum())

# Caso precise remover alguma linha ou preencher valores ausentes, utilizar o código abaixo
# Exemplo de tratamento:
#df = df.dropna()  # Remove linhas com valores ausentes
# ou
#df['coluna'] = df['coluna'].fillna(valor)  # Preenche valores ausentes

# %%
# Verifica valores duplicados
print(df.duplicated().sum())
#df = df.drop_duplicates()

# %%
# Vendas totais por categoria
df_categ = df.groupby(['Category'])['Sales'].sum()
df_categ

# %%
# Top 10 subcategorias mais vendidas
df_subc = df.groupby(['Sub-Category'])['Sales'].sum().sort_values(ascending=False).head(10)
df_subc

# %%
# Gráfico de Barras para Vendas por Categoria

import matplotlib.pyplot as plt

df_categ.plot(kind='bar')
plt.title('Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.show()