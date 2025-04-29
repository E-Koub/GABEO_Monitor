import streamlit as st
import pandas as pd

import sys
import os
import streamlit as st
from src.automate.preparation.automates_cleaner import clean_automates_data
from src.automate.ingestion import load_raw_automates_data

def show(context):  # fonction attendue dans la structure ROUTES
    st.title("📊 Analyse des Automates")
    # Étape 1 : Ingestion
    df_raw = load_raw_automates_data()
    df = clean_automates_data(df_raw)

    st.write("Aperçu des données brutes :", df.head())




