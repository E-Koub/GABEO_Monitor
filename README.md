# GABEO Monitor : Pilotage, Supervision et Maintenance Prédictive des Automates Bancaires par la Data

## 📌 Contexte

Ce projet s'inscrit dans une logique de supervision et d’optimisation du parc d’automates bancaires (GAB, DAB, etc.) déployé 
dans les établissements du groupe Crédit Mutuel Alliance Fédérale, ainsi que leurs partenaires (SG, BNPP, E.Leclerc…).  
La solution GABEO est utilisée pour piloter ces automates, et ce projet propose une **approche data-driven** pour améliorer :

- La **disponibilité** des automates
- La **détection** des incidents
- La **prévision** des maintenances
- Le **pilotage** décisionnel par KPIs et visualisations**

---

## 🎯 Objectifs du projet

- Centraliser et structurer les données de supervision des automates
- Visualiser les KPIs opérationnels clés dans un dashboard interactif
- Identifier les automates à risque ou en sous-performance
- Prédire les incidents grâce à des modèles de machine learning simples
- Fournir un outil d’aide à la décision pour les équipes IT, support et métier

---

## 🛠️ Stack Technique

| Composant | Outils / Technologies |
|----------|------------------------|
| Langage principal | Python 3 |
| Analyse de données | Pandas, NumPy |
| Visualisation | Seaborn, Plotly, Matplotlib |
| Dashboard | Streamlit (ou Power BI en option) |
| Modélisation prédictive | Scikit-learn |
| Base de données | PostgreSQL / SQLite (selon le besoin) |
| Géolocalisation (carte) | Folium |

---

## 🧪 Données simulées

Le projet utilise des données simulées représentant :
- Un parc d’automates : ID, localisation, modèle, fournisseur
- Des journaux de disponibilité/incidents
- Des volumes de transactions (retraits, dépôts, consultations)
- Des tickets de maintenance

📁 Dossier `data/` : contient les jeux de données `.csv` utilisés dans le projet.

---

## 📊 Fonctionnalités du Dashboard

- 🔍 **Monitoring en temps réel** : statut des automates (fonctionnels / en panne)
- 📈 **KPIs clés** : taux de disponibilité, délai moyen de résolution, etc.
- 📍 **Carte interactive** : localisation et état des automates par région
- 🧠 **Maintenance prédictive** : classification des automates à risque
- 📊 **Analyse transactionnelle** : activité par automate, période, banque, etc.
- 🏆 **Classement** : top automates / sous-performants

---

## 📁 Structure du projet

