from vendor.dataHive.utils.ingestion.loader import load_csv_file, save_file
import logging
import pandas as pd


def ingest_automates():
    
    df = load_csv_file('automates',';') 
    if df is None:
        logging.error("Echec chargement fichier automates")
        return

    expected_columns = [
        'Réseau', 'Code Etablissement', 'Etablissement', 'Code agence', 'Agence',
        'Adresse', 'Ville', 'Code postal', 'Emplacement', 'Horaires Automate',
        'Typologie', 'Etat de fonctionnement', 'point_geographique'
    ]
    missing_cols = [col for col in expected_columns if col not in df.columns]
    if missing_cols:
        logging.error(f"Colonnes manquantes: {missing_cols}")
        raise ValueError(f"Colonnes manquantes: {missing_cols}")
    
    string_cols = ['Réseau', 'Etablissement', 'Agence', 'Ville', 'Emplacement', 'Typologie', 'Etat de fonctionnement']
    for col in string_cols:
        df[col] = df[col].str.strip().str.title()

    df['Etat de fonctionnement'] = df['Etat de fonctionnement'].str.lower()

    df = df.drop_duplicates(subset=['Code Etablissement', 'Code agence', 'Emplacement'])
   
    def split_coordinates_gps(row):
        try:
            lat, lon = row.split(',')
            return float(lat.strip()), float(lon.strip())
        except Exception as e:
            logging.warning(f"Coordonnées invalides : {row} ({e})")
            return None, None

    df[['latitude', 'longitude']] = df['point_geographique'].apply(
        lambda x: pd.Series(split_coordinates_gps(x))
    )

    missing_coords = df[['latitude', 'longitude']].isnull().sum().sum()
    if missing_coords > 0:
        logging.warning(f"{missing_coords} coordonnées GPS manquantes ou invalides détectées")

    logging.info(f"Ingestion automates: {df.shape[0]} lignes après nettoyage")

    save_file(df, 'automates')
if __name__ == "__main__":
    ingest_automates()
