# Variables
APP_NAME=gabéo-monitor
PORT=8501

# Construction de l'image Docker
build:
	docker build -t $(APP_NAME) .

# Lancement du conteneur Docker (sans base de données)
run:
	docker run -p $(PORT):8501 $(APP_NAME)

# Démarrage avec Docker Compose (avec PostgreSQL)
up:
	docker compose up -d --build

# Arrêt complet
down:
	docker compose down

# Importation du CSV vers PostgreSQL
import:
	docker compose exec dashboard python src/db/load_csv_to_postgres.py

# Nettoyage (arrêt + volumes)
clean:
	docker compose down -v

# Lint (optionnel si tu ajoutes flake8/black)
lint:
	black src dashboard
	flake8 src dashboard
