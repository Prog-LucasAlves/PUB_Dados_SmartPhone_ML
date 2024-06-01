# Bibliotecas utilizadas
import streamlit as st
import pandas as pd
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('./data/data.db')

# Consulta ao banco de dados para obter os dados tabela 'ML'
df = pd.read_sql_query("SELECT * FROM ML", conn)

# Fechar a conexão com o banco de dados
conn.close()

# Título da aplicação
st.title("Pesquisa de Mercado - :blue[_Smartphones no Mercado Livre._📱]")

# Layout com colunas para KPIs
st.subheader("KPIs Principais do Sistema")
col1, col2, col3 = st.columns(3)

# KPI 1 - Quantidade de smartphones
total_itens = df.shape[0]
col1.metric(label="Número Total de Smartphones", value=total_itens)

# KPI 2: Número de lojas únicas
unique_lojas = df['loja'].nunique()
col2.metric(label="Número de Lojas Únicas", value=unique_lojas)

# KPI 3: Preço médio novo (em reais)
average_new_price = df['new_price'].mean()
col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

# Quais as lojas são mais encontradas até a 10ª página
st.subheader('Lojas Mais Encontradas até a 20ª Página')
col1, col2 = st.columns([6, 4])
top_10_pages_lojas = (df['loja'].value_counts()
                      .sort_values(ascending=False)
                      .reset_index()
                      .rename(columns={'loja': 'Loja', 'count': 'Qtd'}))
col1.bar_chart(top_10_pages_lojas, x='Loja', y='Qtd')
col2.write(top_10_pages_lojas)

# Qual o preço médio por loja
st.subheader('Preço Médio por Loja')
col1, col2 = st.columns([6, 4])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_lojas = (df_non_zero_prices.groupby('loja')['new_price']
                          .mean()
                          .sort_values(ascending=False)
                          .reset_index()
                          .rename(columns={'loja': 'Loja', 'new_price': 'Preço Médio'}))
col1.bar_chart(average_price_by_lojas, x='Loja', y='Preço Médio')
col2.write(average_price_by_lojas)

# Qual a satisfação por Loja
st.subheader('Satisfação por Loja')
col1, col2 = st.columns([6, 4])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = (df_non_zero_reviews.groupby('loja')['reviews_rating_number']
                         .mean()
                         .round(2)
                         .sort_values(ascending=False)
                         .reset_index()
                         .rename(columns={'loja': 'Loja', 'reviews_rating_number': 'Satisfação'}))
col1.bar_chart(satisfaction_by_brand, x='Loja', y='Satisfação')
col2.write(satisfaction_by_brand)
