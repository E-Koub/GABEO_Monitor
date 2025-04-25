import pandas as pd
from dataclasses import dataclass
from sklearn.cluster import KMeans

@dataclass
class Automate:
    
    def __init__(self, data: pd.DataFrame):
            self.data = data
            
    def cluster_automates(df):
        kmeans = KMeans(n_clusters=3)
        df['cluster'] = kmeans.fit_predict(df[['nb_incidents_30j', 'nb_transactions_journalier']])
        return df
