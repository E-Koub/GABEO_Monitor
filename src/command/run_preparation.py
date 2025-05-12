# src/command/run_preparation.py

import logging
import sys
import os


import sys
import os

os.environ['SETTINGS_PATH'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','../config/settings.yaml'))

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from automate.preparation.automates_prepare import prepare_automates

logging.basicConfig(level=logging.INFO)

def main():
    prepare_automates()

if __name__ == "__main__":
    main()
