# src/automate/preparation/automates_prepare.py

import pandas as pd
import os
import logging
import datetime
import numpy as np
from vendor.dataHive.utils.ingestion.loader import load_csv_file, save_file

def prepare_automates():
    logging.info("Préparation des données automates…")
    
    processed_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../data/processed'))
    input_file = os.path.join(processed_dir, 'automates_clean.csv')
    output_file = os.path.join(processed_dir, 'automates_prepared.csv')
    
    df = load_csv_file(input_file,';') 
    incidents_df=None
    
    # NORMALISATIONS DE BASE
    df['Réseau'] = df['Réseau'].str.upper().str.strip()
    df['Ville'] = df['Ville'].str.upper().str.strip()
    df['Code Etablissement'] = pd.to_numeric(df['Code Etablissement'], errors='coerce')
    df['Code agence'] = pd.to_numeric(df['Code agence'], errors='coerce')
    df['Adresse'] = df['Adresse'].str.strip()

    # MAPPING état de fonctionnement
    mapping_etat = {'FONCTIONNEL': 1, 'EN PANNE': 0, 'OPERATIONNEL': 1, 'HORS SERVICE': 0}
    df['Etat_num'] = df['Etat de fonctionnement'].map(mapping_etat)

    # FILTRAGE coord manquantes
    df = df.dropna(subset=['point_geographique'])
    logging.info(f"Après suppression coordonnées manquantes : {df.shape}")

    # SPLIT COORDS
    df[['latitude', 'longitude']] = df['point_geographique'].str.split(',', expand=True).astype(float)

    # VALIDATION COORDONNEES
    df = df[(df['latitude'].between(-90, 90)) & (df['longitude'].between(-180, 180))]
    df = df[(df['latitude'] != 0) & (df['longitude'] != 0)]

    # SUPPRIMER COLONNE ORIGINE
    df = df.drop(columns=['point_geographique'])

    # QUARTIER
    def get_quartier(cp):
        if str(cp).startswith('75'):
            return 'Paris'
        elif str(cp).startswith('69'):
            return 'Lyon'
        elif str(cp).startswith('13'):
            return 'Marseille'
        else:
            return 'Autre'
    df['quartier'] = df['Code postal'].apply(get_quartier)

    # SI COLONNE Derniere_maj
    if 'Derniere_maj' in df.columns:
        X_JOURS = 7
        df['Derniere_maj'] = pd.to_datetime(df['Derniere_maj'], errors='coerce')
        aujourdhui = pd.Timestamp.now()
        df['jours_hors_service'] = (aujourdhui - df['Derniere_maj']).dt.days
        df['hors_service_Xj'] = ((df['Etat_num'] == 0) & (df['jours_hors_service'] > X_JOURS)).astype(int)
    else:
        df['jours_hors_service'] = np.nan
        df['hors_service_Xj'] = np.nan

    # CATEGORIE USAGE (si transactions_total existe)
    if 'transactions_total' in df.columns:
        df['categorie_usage'] = pd.cut(
            df['transactions_total'],
            bins=[-1, 500, 1000, float('inf')],
            labels=['FAIBLE ACTIVITE', 'MOYENNE ACTIVITE', 'HAUTE ACTIVITE']
        )

    # SCORE PERFORMANCE (si colonnes nécessaires)
    if 'transactions_total' in df.columns:
        max_tx = df['transactions_total'].max() or 1
        df['score_performance'] = (
            (df['Etat_num'].fillna(0) * 0.5) +
            ((1 - df['jours_hors_service'].fillna(0) / 30).clip(0, 1) * 0.3) +
            ((df['transactions_total'] / max_tx) * 0.2)
        )
    else:
        df['score_performance'] = np.nan

    # INCIDENTS (optionnel si incidents_df fourni)
    if incidents_df is not None:
        incidents_recent = incidents_df[incidents_df['date_incident'] >= (pd.Timestamp.now() - pd.Timedelta(days=30))]
        counts = incidents_recent.groupby('id_automate').size().reset_index(name='nb_incidents_30j')
        df = df.merge(counts, how='left', left_on='id_automate', right_on='id_automate')
        df['multi_incidents_30j'] = (df['nb_incidents_30j'].fillna(0) >= 3).astype(int)
    else:
        df['nb_incidents_30j'] = np.nan
        df['multi_incidents_30j'] = np.nan

    # DISTANCE AU CENTRE (Paris)
    from math import radians, sin, cos, sqrt, atan2
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371
        dlat, dlon = radians(lat2 - lat1), radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        return 2 * R * atan2(sqrt(a), sqrt(1 - a))
    CENTRE_LAT, CENTRE_LON = 48.85, 2.35
    df['distance_centre'] = df.apply(lambda r: haversine(r['latitude'], r['longitude'], CENTRE_LAT, CENTRE_LON), axis=1)

    logging.info(f"Données automates préparées → shape finale : {df.shape}")
    
    
    # Sauvegarde
    save_file(df, output_file)
    logging.info(f"Données préparées sauvegardées → {output_file}")
    
    return df

