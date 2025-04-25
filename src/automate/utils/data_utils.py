import pandas as pd

def clean_automates_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie le DataFrame contenant les données d'automates."""

    df = df.copy()
    return df