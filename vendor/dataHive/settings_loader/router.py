import yaml
import importlib
from pathlib import Path

# Chemin du fichier YAML contenant la configuration des routes
ROUTES_YAML = Path(__file__).parent / "config/routes.yaml"

def load_routes():
    with open(ROUTES_YAML, "r") as f:
        config = yaml.safe_load(f)

    # Chargement de la route par défaut
    default = config["default"]
    routes = {}

    # Chargement de chaque route à partir du YAML
    for route, route_info in config["routes"].items():
        module = importlib.import_module(route_info["module"])
        func = getattr(module, route_info["function"])
        routes[route] = {
            "label": route_info["label"],
            "view": func
        }

    return routes, default

# Charge les routes et la route par défaut
ROUTES, DEFAULT_ROUTE = load_routes()
