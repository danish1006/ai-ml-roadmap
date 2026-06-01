import pandas as pd
from src.utils.helpers import load_config


def categorize(merchant, categories_config):
    """
    Categorizes a merchant using config-driven keyword matching.

    Args:
        merchant (str): Merchant name.
        categories_config (dict): Category-to-merchant mapping.

    Returns:
        str: Business category name.
    """
    merchant = str(merchant).lower()

    for category, merchants in categories_config.items():
        if any(m.lower() in merchant for m in merchants):
            return category

    return "Other"


def clean_data(df):
    """
    Cleans and standardizes transaction data.

    Operations:
    - Handles missing merchant values
    - Removes extra spaces
    - Converts merchant names to lowercase
    - Converts amount column to numeric safely

    Args:
        df (pd.DataFrame): Raw transaction dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    df["merchant"] = (
        df["merchant"]
        .fillna("Unknown")
        .str.strip()
        .str.lower()
    )

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    return df


def engineer_features(df):
    """
    Creates derived transaction features.

    Features created:
    - invalid_amount
    - negative_amount
    - high_value
    - transaction_type

    Args:
        df (pd.DataFrame): Cleaned transaction dataframe.

    Returns:
        pd.DataFrame: Feature-enriched dataframe.
    """
    df["invalid_amount"] = df["amount"].isnull()

    df["negative_amount"] = df["amount"] < 0

    df["high_value"] = df["amount"] > 5000

    df["transaction_type"] = df["amount"].apply(
        lambda x: (
            "Invalid" if pd.isnull(x)
            else "Credit" if x >= 50000
            else "Refund" if x < 0
            else "Debit"
        )
    )

    return df


def run_analysis(df):
    """
    Runs transaction-level summary analysis and prints data quality metrics.

    Args:
        df (pd.DataFrame): Processed transaction dataframe.
    """
    print("\n=== Transaction Summary by Category ===")
    print(df.groupby("category")["amount"].mean())

    print("\n=== Transaction Count by Type ===")
    print(df.groupby("transaction_type").size())

    print("\n=== Invalid Transactions ===")
    print(df[df["invalid_amount"]])

    print("\n=== Unknown Category Transactions ===")
    print(df[df["unknown_category"]])

    print("\n=== Data Quality Summary ===")
    print(f"Total transactions: {len(df)}")
    print(f"Invalid amounts: {df['invalid_amount'].sum()}")
    print(f"Unknown categories: {df['unknown_category'].sum()}")
    print(f"High value transactions: {df['high_value'].sum()}")


def parse_transactions(file_path, config_path):
    """
    Main transaction parsing pipeline.

    Workflow:
    - Loads configuration
    - Reads transaction CSV
    - Validates input data
    - Cleans data
    - Engineers features
    - Categorizes merchants
    - Runs analysis

    Args:
        file_path (str): Path to input CSV file.
        config_path (str): Path to config.yaml.

    Returns:
        pd.DataFrame: Fully processed transaction dataframe.
    """
    print(f"Reading file: {file_path}")

    config = load_config(config_path)
    categories_config = config["categories"]

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error reading input file: {e}")

    if df.empty:
        raise ValueError("Input CSV file is empty.")

    required_columns = ["merchant", "amount"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    df = clean_data(df)

    df = engineer_features(df)

    df["category"] = df["merchant"].apply(
        lambda x: categorize(x, categories_config)
    )

    df["unknown_category"] = df["category"] == "Other"

    run_analysis(df)

    return df