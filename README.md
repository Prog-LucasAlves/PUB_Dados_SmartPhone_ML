# Realizando Captura de Dados de SmartPhones do Mercado Livre

## Descrição

- Irei utilizar a biblioteca [SCRAPY](https://scrapy.org/), para realizar a captura dos dados, após vou utilizar biblioteca [PANDAS](https://pandas.pydata.org/) para limpar/analisar os dados, e para finalizar o [STREAMLIT](https://streamlit.io/) para visualização do dados.

- Site que irei coletar os dados [SITE](https://lista.mercadolivre.com.br/celulares-telefones)

## Python

- Versão do python utilizada: **3.12.1** | atraves do *pyenv*
- Arguivo .python-version
Ref.: [pyenv](https://github.com/pyenv/pyenv)

## Criando diretório para o projeto

```bash
mkdir dataproject
cd dataproject
```

## Clonando o repositório

```bash
git clone https://github.com/Prog-LucasAlves/PUB_Dados_SmartPhone_ML.git
```

## Criando ambiente virtual(poetry)

```bash
poetry shell
```

Ref.: [poetry](https://python-poetry.org/)

## Instalando as dependências do projeto

```bash
poetry install
```

## Utilizando o Scrapy

```bash
scrapy startproject <nomedoprojeto>
```
