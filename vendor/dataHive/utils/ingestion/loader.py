import pandas as pd
import os
import logging
import yaml


SETTINGS_PATH = os.environ.get('SETTINGS_PATH')
if SETTINGS_PATH is None:
    raise FileNotFoundError("La variable d'environnement SETTINGS_PATH n'est pas définie")

try:
    with open(SETTINGS_PATH, 'r') as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    logging.error(f"Le fichier de configuration est introuvable : {SETTINGS_PATH}")
    raise
except yaml.YAMLError as e:
    logging.error(f"Erreur de parsing YAML dans le fichier {SETTINGS_PATH} : {e}")
    raise
except Exception as e:
    logging.error(f"Erreur inattendue lors du chargement de {SETTINGS_PATH} : {e}")
    raise

RAW_PATH = config['paths']['raw_data']
PROCESSED_PATH = config['paths']['processed_data']

# Logger
logging.basicConfig(
    filename='data/logs/ingestion.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def load_csv_file(file_name, sep,folder=RAW_PATH):
        
    if not file_name.endswith('.csv'):
        file_name += '.csv'
    file_path = os.path.join(folder, file_name)
   
    try:
        df = pd.read_csv(file_path, sep=sep, encoding='utf-8-sig')
        print(f"Fichier chargé: {file_name} ({df.shape[0]} lignes, {df.shape[1]} colonnes)")
        logging.info(f"Fichier chargé: {file_name} ({df.shape[0]} lignes, {df.shape[1]} colonnes)")
        return df
    except Exception as e:
        logging.error(f"Erreur chargement {file_name}: {str(e)}")
        return None

def save_file(df, name, folder=PROCESSED_PATH):
    processed_file = os.path.join(folder, f"{name}_clean.csv")
    df.to_csv(processed_file, sep=';', index=False)
    logging.info(f"Fichier sauvegardé: {processed_file}")
