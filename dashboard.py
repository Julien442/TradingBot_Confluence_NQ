
import streamlit as st
import pandas as pd
from utils import load_csv, detect_confluences
from ibkr_connector import send_market_order, send_limit_order, send_trailing_stop

st.set_page_config(layout="wide")

st.title("🧠 TradingBot DOM / TAS / ICT - Confluence Tracker")

# Filtres
min_dom = st.sidebar.slider("Taille DOM minimale", 1, 100, 10)
min_tas = st.sidebar.slider("Volume TAS minimal", 1, 100, 10)
type_tx = st.sidebar.selectbox("Type de transaction", ["All", "Buy", "Sell"])

# Chargement des données
dom = load_csv("data/DOM.csv")
tas = load_csv("data/TimeAndSales.csv")

# Application des filtres
dom_filt = dom[dom["AskSize"] > min_dom]
tas_filt = tas[tas["Volume"] > min_tas]
if type_tx != "All":
    tas_filt = tas_filt[tas_filt["Type"] == type_tx]

# Détection des confluences
confluences = detect_confluences(dom_filt, tas_filt)

st.subheader("📊 Alertes")
st.write("### ✅ DOM (Filtered)")
st.dataframe(dom_filt)
st.write("### ✅ Time & Sales (Filtered)")
st.dataframe(tas_filt)

if st.button("📌 Analyser les confluences"):
    st.write("### 🔥 Confluences détectées")
    st.dataframe(confluences)

    if not confluences.empty:
        if st.button("🟢 Exécuter un ordre marché"):
            send_market_order("BUY", confluences.iloc[-1]["BidPrice"])

        if st.button("🟡 Placer un ordre limite"):
            send_limit_order("BUY", confluences.iloc[-1]["BidPrice"] - 1)

        if st.button("🔵 Placer un trailing stop"):
            send_trailing_stop("BUY", confluences.iloc[-1]["BidPrice"], 1.5)

st.write("### 📔 Journal de Confluence Pondéré")
try:
    st.dataframe(pd.read_csv("data/Journal.csv"))
except:
    st.warning("Pas encore de journal généré.")
