import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Dados", layout="wide")

st.title("📊 Dashboard Automático")

arquivo = st.file_uploader("Envie um arquivo Excel ou CSV")

if arquivo is not None:

    # ler arquivo
    if arquivo.name.endswith(".csv"):
        df = pd.read_csv(arquivo)
    else:
        df = pd.read_excel(arquivo)

    st.subheader("📋 Dados")
    st.dataframe(df)

    # selecionar apenas colunas numéricas
    colunas_numericas = df.select_dtypes(include="number").columns

    if len(colunas_numericas) > 0:

        st.subheader("📈 Estatísticas")

        stats = pd.DataFrame({
            "Média": df[colunas_numericas].mean(),
            "Soma": df[colunas_numericas].sum(),
            "Maior": df[colunas_numericas].max(),
            "Menor": df[colunas_numericas].min()
        })

        st.dataframe(stats)

        st.subheader("📊 Gráfico")

        coluna = st.selectbox("Escolha a coluna", colunas_numericas)

        fig, ax = plt.subplots()
        df[coluna].plot(kind="bar", ax=ax)
        st.pyplot(fig)

    else:
        st.warning("Não há colunas numéricas para análise")
