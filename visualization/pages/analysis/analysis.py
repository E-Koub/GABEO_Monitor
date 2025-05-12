# visualization/pages/analysis.py
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os


from src.automate.analysis.automate_analyzer import AutomateAnalyzer

def show(context):
    st.title("📊 Analyse Exploratoire des Automates")

    analyzer = AutomateAnalyzer()
    df = analyzer.get_data()

    # Statistiques descriptives
    st.header("Statistiques descriptives")
    st.write(df.describe())
        


