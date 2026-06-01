import yaml


def load_config(config_path):
    """
    Loads YAML configuration file.

    Args:
        config_path (str): Path to config.yaml

    Returns:
        dict: Parsed configuration dictionary
    """
    try:
        with open(
            config_path,
            "r",
            encoding="utf-8"
        ) as file:
            return yaml.safe_load(file)

    except Exception as e:
        raise Exception(
            f"Error loading config file: {e}"
        )