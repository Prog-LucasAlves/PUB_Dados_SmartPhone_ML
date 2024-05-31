# Bibliotecas utilizadas
import pandas as pd
import sqlite3
from datetime import datetime

# Caminho do arquivo JSON
df = pd.read_json('../../data/data.jsonl', lines=True)

print(df.head(5))

# Mostrar todas as colunas
pd.options.display.max_columns = None

# Adicionar a coluna _source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/smatphonnes#D[A:smatphonnes]"

# Adicionar a coluna _timestamp com o valor atual
df['_data_coleta'] = datetime.now()

# Tratar valores nulos para colunas numéricas e texto
df['old_preco_reais'] = df['old_preco_reais'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Remover os parênteses das colunas 'reviews_amount'
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(float)

# Tratar os preços como float e calcular os valores totais
df['old_price'] = df['old_preco_reais']
df['new_price'] = df['new_price_reais']

# Remover as linhas com valores nulos
df.dropna(inplace=True)

# Filtro para os smartphones que tenham preços anteriores maiores
df = df[df['old_price'] > df['new_price']]

# Filtro para os smartphones que tenham preços sucessores menores
df['x10'] = df['old_price'] / 10
df['x10'] = df['x10'].astype(int)
df['x20'] = df['new_price']
df['x20'] = df['x20'].astype(int)

df = df[df['x10'] != df['x20']]

# Remover a parte 'por ' do campo 'loja'
df['loja'] = df['loja'].str.lstrip('por ')

# Remover as colunas que não serão utilizadas
df.drop(columns=['old_preco_reais', 'new_price_reais', 'x10', 'x20'], axis=1, inplace=True)

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('../../data/data.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('ML', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()
df.to_csv('../../data/data.csv', index=False)

print(df.head())
