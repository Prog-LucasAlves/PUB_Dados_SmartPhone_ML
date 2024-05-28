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

# Configuração CSS
tabs_font_css = """
<style>
    div[class*=stTitle] label{
        font-size: 26px;
        color: blue
}
</style>


"""
st.markdown(tabs_font_css, unsafe_allow_html=True)

# Título da aplicação
st.title("Pesquisa de Mercado - :blue[_Smartphones no Mercado Livre_]")
