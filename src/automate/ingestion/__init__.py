import pandas as pd
from pathlib import Path

def load_raw_automates_data(data_dir: str = "data/raw", filename: str = "automates.csv") -> pd.DataFrame:
    """
    Charge les données brutes des automates depuis un fichier CSV.

    Args:
        data_dir (str): Répertoire des données brutes.
        filename (str): Nom du fichier CSV.

    Returns:
        pd.DataFrame: Données chargées sous forme de DataFrame.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'est pas trouvé.
        pd.errors.ParserError: Si le fichier n'est pas au format CSV valide.
    """
    # Création du chemin complet du fichier
    file_path = Path(data_dir) / filename
    
    # Vérification si le fichier existe
    if not file_path.exists():
        raise FileNotFoundError(f"Fichier non trouvé : {file_path}")
    
    try:
        # Lecture du fichier CSV
        df = pd.read_csv(file_path)
        return df
    except pd.errors.ParserError:
        raise ValueError(f"Erreur de formatage dans le fichier : {file_path}")
    except Exception as e:
        raise RuntimeError(f"Une erreur est survenue lors de la lecture du fichier {file_path}: {str(e)}")
