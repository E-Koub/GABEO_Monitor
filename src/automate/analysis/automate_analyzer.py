# src/automate/analysis/automate_analyzer.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

class AutomateAnalyzer:
    def __init__(self, data_path=None, report_path=None):
        self.data_path = data_path or os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../data/processed/automates_prepared.csv'))
        self.report_path = report_path or os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../reports'))
        self.df = None
        logging.basicConfig(level=logging.INFO)

    def load_data(self):
        logging.info(f"Chargement des données depuis {self.data_path}")
        self.df = pd.read_csv(self.data_path, sep=';')
        return self.df
    
    def get_data(self):
        if self.df is None:
            return self.load_data()
        return self.df

    def analyse_distribution(self):
        logging.info("Analyse des distributions numériques")
        print(self.df.describe())
        print("\nValeurs manquantes :\n", self.df.isnull().sum())

    def analyse_typologie(self):
        logging.info("Analyse des typologies d'automates")
        typologie_counts = self.df['Typologie'].value_counts()
        print(typologie_counts)
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, y='Typologie', order=typologie_counts.index)
        plt.title("Répartition des typologies")
        self._save_plot("typologie_distribution.png")

    def analyse_score(self):
        logging.info("Distribution du score de performance")
        plt.figure(figsize=(10, 5))
        sns.histplot(self.df['score_performance'], bins=20, kde=True)
        plt.title("Score de performance")
        self._save_plot("score_distribution.png")

    def analyse_par_quartier(self):
        logging.info("Analyse des scores par quartier")
        stats = self.df.groupby('quartier')['score_performance'].mean().sort_values()
        print(stats)
        plt.figure(figsize=(10, 5))
        stats.plot(kind='barh')
        plt.title("Score moyen par quartier")
        self._save_plot("score_par_quartier.png")

    def analyse_hors_service(self):
        if 'hors_service_Xj' in self.df.columns:
            count = self.df['hors_service_Xj'].sum()
            logging.info(f"{count} automates sont hors service depuis plus de X jours")

    def _save_plot(self, filename):
        output_file = os.path.join(self.report_path, filename)
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
        logging.info(f"📊 Graphe sauvegardé → {output_file}")
    

    def run_all(self):
        self.load_data()
        self.analyse_distribution()
        self.analyse_typologie()
        self.analyse_score()
        self.analyse_par_quartier()
        self.analyse_hors_service()
