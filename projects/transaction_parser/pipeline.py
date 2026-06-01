import os
from src.data_processing.parser import parse_transactions
from src.utils.helpers import load_config


def run_pipeline():
    """
    Main pipeline orchestration function.

    Workflow:
    - Loads configuration
    - Builds input/output paths
    - Runs transaction parser
    - Saves processed output CSV
    """
    print("Starting pipeline...")

    base_dir = os.path.dirname(__file__)

    config_path = os.path.join(base_dir, "config.yaml")

    config = load_config(config_path)

    input_path = os.path.join(
        base_dir,
        config["input_path"]
    )

    output_path = os.path.join(
        base_dir,
        config["output_path"]
    )

    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    data = parse_transactions(
        input_path,
        config_path
    )

    print("Saving processed data...")

    data.to_csv(output_path, index=False)

    print(f"Output saved to: {output_path}")
    print("Pipeline completed.")