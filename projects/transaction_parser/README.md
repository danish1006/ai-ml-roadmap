# Transaction Parser Pipeline

## Project Overview

This project is a transaction preprocessing pipeline built using Python and Pandas.

The pipeline processes raw financial transaction data and transforms it into a clean, structured, and analysis-ready dataset. It demonstrates core data engineering concepts such as data cleaning, validation, feature engineering, configuration-driven categorization, and automated processing workflows.

### Pipeline Workflow

* Read raw transaction CSV data
* Validate input structure and data quality
* Clean and standardize transaction records
* Categorize merchants using YAML-based configuration
* Engineer transaction-level features
* Generate transaction analysis summaries
* Export processed transaction data to CSV

---

## Features

* Config-driven merchant categorization
* Data cleaning and normalization
* Safe numeric conversion using Pandas
* Missing value handling
* Invalid transaction detection
* Refund transaction detection
* Credit and debit transaction classification
* High-value transaction identification
* Unknown category detection
* Transaction summary analytics
* YAML-based configuration management
* Input validation and error handling

---

## Tech Stack

* Python
* Pandas
* YAML
* Git
* GitHub
* VS Code

---

## Project Structure

```text
projects/transaction_parser/
├── config.yaml
├── input/
│   └── data.csv
├── output/
│   └── processed.csv
├── main.py
├── pipeline.py
└── README.md

src/
├── data_processing/
│   └── parser.py
└── utils/
    └── helpers.py
```

---

## Sample Input

```csv
merchant,amount
Swiggy,250
Amazon,1200
Uber,-200
Salary,50000
```

---

## Sample Output Columns

| Column           | Description                            |
| ---------------- | -------------------------------------- |
| merchant         | Cleaned merchant name                  |
| amount           | Transaction amount                     |
| invalid_amount   | Indicates invalid numeric values       |
| negative_amount  | Indicates negative transactions        |
| high_value       | Indicates transactions above threshold |
| transaction_type | Debit, Credit, Refund, or Invalid      |
| category         | Assigned merchant category             |
| unknown_category | Flag for uncategorized merchants       |

---

## Configuration Example

The categorization logic is controlled through `config.yaml`.

```yaml
categories:

  Food:
    - swiggy
    - zomato

  Shopping:
    - amazon
    - flipkart

  Transport:
    - uber
    - irctc

  Income:
    - salary

  Entertainment:
    - netflix

  Healthcare:
    - medical

  Refund:
    - refund
    - reversal
    - cashback
```

This approach allows new merchants and categories to be added without modifying Python code.

---

## Run Project

From the project root directory:

```bash
PYTHONPATH=. python projects/transaction_parser/main.py
```

---

## Learning Objectives

This project was built to practice and reinforce:

* Python programming fundamentals
* Pandas data manipulation
* Data cleaning techniques
* Feature engineering
* Configuration-driven design
* Input validation
* Error handling
* Project structuring
* Modular programming
* Git and GitHub workflow
* Data engineering best practices

---

## Key Concepts Demonstrated

* Modular project architecture
* Separation of concerns
* Configuration management
* Data validation
* Defensive programming
* Feature engineering
* Reusable utility functions
* Pipeline orchestration

---

## Future Improvements

Potential enhancements for future versions:

* Interactive visualization dashboard
* Automated unit testing with pytest
* Structured logging system
* Fraud detection using machine learning
* Database integration
* REST API deployment
* Cloud deployment
* Real-time transaction processing
* Transaction anomaly detection
* CI/CD pipeline implementation

---

## Author

Built as part of the AI/ML Career Rebuild Roadmap to develop practical skills in Python, data processing, data engineering, and machine learning workflows.
