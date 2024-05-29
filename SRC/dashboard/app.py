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

# KPI 1 - Quantidade de smartphones no mercado
total_itens = df.shape[0]
col1.metric(label="Total de Smartphones", value=total_itens)
