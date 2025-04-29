import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster
from src.automate.preparation.automates_cleaner import clean_automates_data

class AutomateAnalyzer:
    def __init__(self, df: pd.DataFrame):
        """
        Étape 1 : Initialisation avec les données brutes
        """
        self.raw_data = df
        self.cleaned_data = None

    def preprocess(self):
        """
        Étape 2 : Préparation (nettoyage)
        """
        self.cleaned_data = clean_automates_data(self.raw_data)

    def show_status_distribution(self):
        """
        Étape 3 : Visualisation de la répartition des statuts
        """
        if self.cleaned_data is None:
            self.preprocess()
        sns.countplot(data=self.cleaned_data, x='status')
        plt.title("Répartition des statuts d'automates")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def map_automates(self):
        """
        Étape 4 : Cartographie interactive des automates
        """
        if self.cleaned_data is None:
            self.preprocess()

        if self.cleaned_data.empty:
            return None

        map_center = [
            self.cleaned_data.latitude.mean(),
            self.cleaned_data.longitude.mean()
        ]
        m = folium.Map(location=map_center, zoom_start=6)
        marker_cluster = MarkerCluster().add_to(m)

        for _, row in self.cleaned_data.iterrows():
            folium.Marker(
                location=[row.latitude, row.longitude],
                popup=f"Ville: {row.ville}, Status: {row.status}"
            ).add_to(marker_cluster)

        return m

    def get_status_counts(self):
        """
        Étape 5 : Statistiques simples (par statut)
        """
        if self.cleaned_data is None:
            self.preprocess()
        return self.cleaned_data['status'].value_counts()

    def avg_transactions_per_constructeur(self):
        """
        Étape 6 : Moyenne des transactions par constructeur
        """
        if self.cleaned_data is None:
            self.preprocess()
        return self.cleaned_data.groupby('constructeur')['nb_transactions_journalier'].mean().sort_values(ascending=False)

    def incidents_summary(self):
        """
        Étape 7 : Synthèse des incidents récents (>0 sur 30j)
        """
        if self.cleaned_data is None:
            self.preprocess()
        return self.cleaned_data[self.cleaned_data['nb_incidents_30j'] > 0]
