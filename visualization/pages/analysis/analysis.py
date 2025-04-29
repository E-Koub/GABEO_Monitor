import os
import sys
import streamlit as st
from streamlit_folium import st_folium

# Accès aux modules src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.automate.ingestion import load_raw_automates_data
from src.automate.analysis.automate_analyzer import AutomateAnalyzer

def show(context=None):
    st.title("📊 Analyse des Automates")

    # Étape 1 : Ingestion
    df_raw = load_raw_automates_data()
    if df_raw is None or df_raw.empty:
        st.error("❌ Aucune donnée brute trouvée.")
        return

    st.subheader("📄 Données brutes")
    st.dataframe(df_raw.head())

    # Étape 2 : Initialiser l'analyseur et nettoyer
    analyzer = AutomateAnalyzer(df_raw)
    analyzer.preprocess()

    # Étape 3 : Statistiques simples
    st.subheader("📌 Répartition des statuts")
    st.write(analyzer.get_status_counts())

    # Étape 4 : Carte interactive
    st.subheader("🗺️ Carte des automates")
    folium_map = analyzer.map_automates()
    if folium_map:
        st_folium(folium_map, width=700, height=500)
    else:
        st.warning("⚠️ Données géographiques manquantes pour afficher la carte.")

    # Étape 5 : Moyenne des transactions
    st.subheader("💳 Moyenne des transactions par constructeur")
    st.write(analyzer.avg_transactions_per_constructeur())

    # Étape 6 : Synthèse des incidents
    st.subheader("🚨 Automates avec incidents récents")
    st.dataframe(analyzer.incidents_summary())

