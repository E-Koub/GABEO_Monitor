import yaml
import importlib
from pathlib import Path

ROUTES_YAML = Path(__file__).resolve().parent.parent.parent.parent / "config" / "routes.yaml"

def load_routes():
    with open(ROUTES_YAML, "r") as f:
        config = yaml.safe_load(f)

    default = config["default"]
    routes = {}

    for route, route_info in config["routes"].items():
        module = importlib.import_module(route_info["module"])
        func = getattr(module, route_info["function"])
        routes[route] = {
            "label": route_info["label"],
            "view": func
        }

    return routes, default

ROUTES, DEFAULT_ROUTE = load_routes()
