from pathlib import Path
import yaml

def load_config(config_path=None):
    # Use default settings.yaml if no path is provided
    default_path = Path(__file__).parent / "settings.yaml"
    config_file = Path(config_path) if config_path else default_path

    if not config_file.exists():
        raise FileNotFoundError(f"❌ YAML config file missing at: {config_file.resolve()}")

    with config_file.open("r") as f:
        return yaml.safe_load(f)
