import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Vision", layout="wide")

# ===== ESTILO DESIGN MODERNO =====
st.markdown("""
<style>

.stApp{
background: radial-gradient(circle at top,#0f172a,#020617);
color:white;
font-family: 'Segoe UI', sans-serif;
}

.big-title{
font-size:48px;
font-weight:700;
text-align:center;
background: linear-gradient(90deg,#22d3ee,#3b82f6);
-webkit-background-clip:text;
color:transparent;
margin-bottom:30px;
}

.card{
background:rgba(255,255,255,0.05);
padding:25px;
border-radius:16px;
backdrop-filter: blur(12px);
box-shadow:0 0 25px rgba(0,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>🚀 Data Vision Dashboard</div>", unsafe_allow_html=True)

# ===== SIDEBAR =====
st.sidebar.title("⚙️ Controles")
arquivo = st.sidebar.file_uploader("Enviar CSV ou Excel")

if arquivo:

    # leitura inteligente
    if arquivo.name.endswith(".csv"):
        try:
            df = pd.read_csv(arquivo)
        except:
            df = pd.read_csv(arquivo, sep=";", encoding="latin1")
    else:
        df = pd.read_excel(arquivo)

    colunas = df.select_dtypes("number").columns

    if len(colunas) > 0:

        st.markdown("### 📊 Indicadores")

        c1,c2,c3,c4 = st.columns(4)

        c1.markdown(f"<div class='card'><h3>Média</h3><h1>{round(df[colunas].mean().mean(),2)}</h1></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='card'><h3>Soma</h3><h1>{round(df[colunas].sum().sum(),2)}</h1></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='card'><h3>Maior</h3><h1>{round(df[colunas].max().max(),2)}</h1></div>", unsafe_allow_html=True)
        c4.markdown(f"<div class='card'><h3>Menor</h3><h1>{round(df[colunas].min().min(),2)}</h1></div>", unsafe_allow_html=True)

        st.markdown("### 📈 Visualização")

        coluna = st.selectbox("Escolha coluna", colunas)

        fig, ax = plt.subplots(figsize=(12,4))
        df[coluna].plot(color="#22d3ee", linewidth=3)
        ax.set_facecolor("#020617")
        fig.patch.set_facecolor("#020617")

        st.pyplot(fig)

        st.markdown("### 📋 Dados")
        st.dataframe(df)

    else:
        st.warning("Sem colunas numéricas")
