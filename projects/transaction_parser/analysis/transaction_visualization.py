import os
import pandas as pd
import matplotlib.pyplot as plt


def create_visualizations():
    """
    Creates visualizations from processed transaction data.
    """

    base_dir = os.path.dirname(os.path.dirname(__file__))

    output_file = os.path.join(
        base_dir,
        "output",
        "processed.csv"
    )

    visualization_dir = os.path.join(
        base_dir,
        "visualizations"
    )

    os.makedirs(visualization_dir, exist_ok=True)

    df = pd.read_csv(output_file)

    valid_df = df[df["invalid_amount"] == False]

    # 1. Amount distribution
    plt.figure()
    valid_df["amount"].hist()
    plt.title("Transaction Amount Distribution")
    plt.xlabel("Amount")
    plt.ylabel("Frequency")
    plt.savefig(
        os.path.join(
            visualization_dir,
            "amount_distribution.png"
        )
    )
    plt.close()

    # 2. Transaction count by category
    plt.figure()
    valid_df["category"].value_counts().plot(kind="bar")
    plt.title("Transaction Count by Category")
    plt.xlabel("Category")
    plt.ylabel("Transaction Count")
    plt.tight_layout()
    plt.savefig(
        os.path.join(
            visualization_dir,
            "transaction_count.png"
        )
    )
    plt.close()

    # 3. Total spending by category
    spending_df = valid_df[valid_df["amount"] > 0]

    plt.figure()
    spending_df.groupby("category")["amount"].sum().plot(kind="bar")
    plt.title("Total Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.savefig(
        os.path.join(
            visualization_dir,
            "category_spending.png"
        )
    )
    plt.close()

    # 4. Category share
    plt.figure()
    valid_df["category"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Category Share")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(
        os.path.join(
            visualization_dir,
            "category_share.png"
        )
    )
    plt.close()


    # 5. Transaction type distribution
    plt.figure()
    df["transaction_type"].value_counts().plot(kind="bar")
    plt.title("Transaction Type Distribution")
    plt.xlabel("Transaction Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(
        os.path.join(
            visualization_dir,
            "transaction_type.png"
        )
    )
    plt.close()

    print("Visualizations created successfully.")


if __name__ == "__main__":
    create_visualizations()