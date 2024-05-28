# Bibliotecas utilizadas
import streamlit as st
import pandas as pd
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('../data/data.db')

# Consulta ao banco de dados para obter os dados tabela 'ML'
df = pd.read_sql_query("SELECT * FROM ML", conn)

# Fechar a conexão com o banco de dados
conn.close()

# Título da aplicação
st.title('Pesquisa de Mercado - Smartphones no Mercado Livre')
