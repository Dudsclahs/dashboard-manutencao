
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
@st.cache_data
def carregar_dados():
    arquivo = "analise_manutencao.xlsx"
    with pd.ExcelFile(arquivo) as xls:
        falhas = pd.read_excel(xls, 'Top Quebras')
        tempo = pd.read_excel(xls, 'Top Tempo Parado')
        tipo_manutencao = pd.read_excel(xls, 'Tipo Manutenção')
        modelos = pd.read_excel(xls, 'Modelos Frequentes')
        tipos_frota = pd.read_excel(xls, 'Tipos de Frota')
        tendencia = pd.read_excel(xls, 'Tendência Mensal')
    return falhas, tempo, tipo_manutencao, modelos, tipos_frota, tendencia

# Inicializa o app
st.title("Dashboard de Manutenção de Equipamentos")

# Carregar dados
falhas, tempo, tipo_manutencao, modelos, tipos_frota, tendencia = carregar_dados()

# Seção 1: Equipamentos que mais quebram
st.header("Equipamentos que Mais Quebram")
st.bar_chart(falhas.set_index('Número de frota')['Quantidade de Falhas'])

# Seção 2: Equipamentos com maior tempo parado
st.header("Equipamentos com Maior Tempo Parado")
st.bar_chart(tempo.set_index('Número de frota')['Tempo Total Parado'])

# Seção 3: Distribuição por Tipo de Manutenção
st.header("Distribuição por Tipo de Manutenção")
st.bar_chart(tipo_manutencao.set_index('Tipo de Manutenção')['Quantidade'])

# Seção 4: Modelos mais frequentes
st.header("Modelos de Equipamentos mais Frequentes")
st.bar_chart(modelos.set_index('Modelo de Equipamento')['Quantidade de Ocorrências'])

# Seção 5: Tipos de Frota com mais Ocorrências
st.header("Tipos de Frota com Mais Ocorrências")
st.bar_chart(tipos_frota.set_index('Tipo de Frota')['Quantidade de Ocorrências'])

# Seção 6: Tendência Mensal
st.header("Tendência Mensal de Manutenções")
st.line_chart(tendencia.set_index('Ano/Mês')['Quantidade de Manutenções'])
