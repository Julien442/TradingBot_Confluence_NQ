# 🤖 TradingBot_Confluence_NQ

Bot de trading avancé basé sur les confluences entre signaux DOM, Time & Sales et stratégie ICT (Market Structure Shift, Fair Value Gap, Order Block).

## 🔍 Fonctionnalités

- Export tick-by-tick DOM & TAS depuis Sierra Chart (via DLL custom)
- Analyse automatisée de confluences avec filtrage (taille min DOM, TAS)
- Journal pondéré des signaux
- Exécution possible (market, limit, trailing) via IBKR
- Interface graphique Streamlit
- Déploiement cloud via Streamlit Cloud

## 📦 Contenu du repo

- `dashboard.py` : interface principale
- `core/` : logique de traitement DOM / TAS / ICT
- `ExportDOMAndTimeAndSales_clean_64.dll` : export Sierra Chart
- `Journal.csv` : journal des signaux simulés
- `requirements.txt` : dépendances Python

## 🚀 Déploiement Streamlit Cloud

1. Fork/clone ce repo
2. Va sur [share.streamlit.io](https://share.streamlit.io/)
3. Renseigne :
   - **Repo** : `Julien442/TradingBot_Confluence_NQ`
   - **Branch** : `main`
   - **Main file path** : `dashboard.py`

## ✅ Dépendances

```bash
pip install -r requirements.txt
