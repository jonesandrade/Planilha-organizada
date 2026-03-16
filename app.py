import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===== CONFIGURAÇÃO =====
st.set_page_config(page_title="Dashboard Futurista", layout="wide")

# ===== ESTILO TECNOLÓGICO =====
st.markdown("""
<style>
.stApp{
background: linear-gradient(180deg,#05070d,#0b1220);
color:white;
}
h1{
text-align:center;
color:#00F0FF;
text-shadow:0 0 25px #00F0FF;
}
.metric-container{
background:#0e1624;
padding:20px;
border-radius:12px;
box-shadow:0 0 15px #00F0FF33;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Dashboard Inteligente de Dados")

# ===== UPLOAD =====
arquivo = st.file_uploader("📂 Envie Excel ou CSV")

if arquivo is not None:

    # ===== LEITOR INTELIGENTE =====
    if arquivo.name.endswith(".csv"):
        try:
            df = pd.read_csv(arquivo)
        except:
            try:
                df = pd.read_csv(arquivo, sep=";", encoding="latin1")
            except:
                df = pd.read_csv(arquivo, sep=";", encoding="utf-8")
    else:
        df = pd.read_excel(arquivo)

    st.success("✅ Arquivo carregado")

    st.subheader("📋 Visualização")
    st.dataframe(df)

    colunas_num = df.select_dtypes(include="number").columns

    if len(colunas_num) > 0:

        st.subheader("📊 Indicadores")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Média", round(df[colunas_num].mean().mean(),2))
        c2.metric("Soma", round(df[colunas_num].sum().sum(),2))
        c3.metric("Maior valor", round(df[colunas_num].max().max(),2))
        c4.metric("Menor valor", round(df[colunas_num].min().min(),2))

        st.subheader("📈 Gráfico automático")

        coluna = st.selectbox("Escolha a coluna", colunas_num)

        fig, ax = plt.subplots(figsize=(12,4))
        df[coluna].plot(color="#00F0FF", linewidth=3)

        ax.set_facecolor("#05070d")
        fig.patch.set_facecolor("#05070d")

        st.pyplot(fig)

    else:
        st.warning("⚠️ Nenhuma coluna numérica encontrada")
