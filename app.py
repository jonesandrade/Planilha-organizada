import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# ====== FUNDO TECNOLÓGICO ======
st.markdown("""
<style>
.stApp{
background: linear-gradient(180deg,#05070d,#0b1220);
color:white;
}

.block-container{
padding-top:2rem;
}

h1{
text-align:center;
color:#00F0FF;
text-shadow:0 0 20px #00F0FF;
}

.css-1d391kg{
background-color:#0b1220;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Dashboard Futurista")

arquivo = st.file_uploader("Enviar planilha")

if arquivo:
    df = pd.read_csv(arquivo)

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("📊 Média", round(df.mean().mean(),2))
    col2.metric("📈 Soma", round(df.sum().sum(),2))
    col3.metric("🔥 Maior", round(df.max().max(),2))
    col4.metric("❄️ Menor", round(df.min().min(),2))

    coluna = st.selectbox("Escolha coluna", df.select_dtypes("number").columns)

    fig, ax = plt.subplots(figsize=(10,4))
    df[coluna].plot(color="#00F0FF", linewidth=3)
    ax.set_facecolor("#05070d")
    st.pyplot(fig)
