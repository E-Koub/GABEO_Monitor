# src/command/run_ingestion.py

import logging
import sys
import os

os.environ['SETTINGS_PATH'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','../config/settings.yaml'))

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from automate.ingestion.automates_ingest import ingest_automates


def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    logging.info("🚀 Début de l'ingestion des données")

    try:
        ingest_automates()
        logging.info("✅ Ingestion terminée avec succès")
    except Exception as e:
        print(f">>> Exception levée: {e}")
        logging.exception(f"❌ Erreur lors de l'ingestion: {e}")


if __name__ == '__main__':
    main()
