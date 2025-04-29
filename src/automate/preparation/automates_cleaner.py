import pandas as pd

def clean_automates_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie les données des automates :
    - Supprime les lignes avec coordonnées ou statut manquants.

    Args:
        df (pd.DataFrame): Données brutes.

    Returns:
        pd.DataFrame: Données nettoyées.
    """
    df = df.dropna(subset=['latitude', 'longitude', 'status'])
    return df
