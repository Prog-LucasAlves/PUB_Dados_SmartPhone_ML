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
st.title("Pesquisa de Mercado - :blue[_Smartphones no Mercado Livre._]")

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
