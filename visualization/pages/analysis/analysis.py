import os
import sys
import streamlit as st
from streamlit_folium import st_folium

# Accès aux modules src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def show(context=None):
    st.title("📊 Analyse des Automates")

