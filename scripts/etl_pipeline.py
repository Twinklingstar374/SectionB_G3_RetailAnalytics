# ETL Pipeline — Retail Analytics
# SectionB Group 3

import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ── Resolve project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / 'data/raw/new_retail_data_2.csv'
PROCESSED_PATH = PROJECT_ROOT / 'data/processed/cleaned_dataset.csv'
TABLEAU_PATH = PROJECT_ROOT / 'data/processed/tableau_ready_dataset.csv'

def extract():
    print("Step 1: Extracting data...")
    df = pd.read_csv(RAW_PATH)
    print(f"Extracted: {df.shape}")
    return df

def transform(df):
    print("Step 2: Transforming data...")

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Drop PII columns
    pii_cols = ['Name', 'Email', 'Phone', 'Address', 'Zipcode']
    df.drop(columns=[c for c in pii_cols if c in df.columns], inplace=True)

    # Fix Date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Date'] = df['Date'].ffill()

    # Fill numeric nulls
    for col in ['Age', 'Amount', 'Total_Amount', 'Ratings']:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    # Fill categorical nulls
    for col in ['Gender', 'Customer_Segment', 'Product_Category',
                'Product_Brand', 'Product_Type', 'Feedback',
                'Shipping_Method', 'Payment_Method', 'Order_Status']:
        if col in df.columns:
            df[col].fillna(df[col].mode()[0], inplace=True)

    # Fill location nulls
    for col in ['City', 'State', 'Country']:
        if col in df.columns:
            df[col].fillna('Unknown', inplace=True)

    # Fill time nulls
    for col in ['Year', 'Month']:
        if col in df.columns:
            df[col].fillna(df[col].mode()[0], inplace=True)

    # Fix avg_order_value inf
    if 'Total_Purchases' in df.columns:
        df['avg_order_value'] = df['Total_Amount'] / df['Total_Purchases'].replace(0, np.nan)
        df['avg_order_value'].fillna(0, inplace=True)
        df['avg_order_value'].replace([float('inf'), -float('inf')], 0, inplace=True)

    # Feature Engineering
    # Age Group
    df['age_group'] = pd.cut(
        df['Age'],
        bins=[0, 25, 35, 45, 60, 100],
        labels=['18-25', '26-35', '36-45', '46-60', '60+']
    )

    # Purchase Category
    df['purchase_category'] = pd.cut(
        df['Total_Purchases'],
        bins=[0, 2, 5, 10, 100],
        labels=['Low', 'Medium', 'High', 'Very High']
    )

    # Revenue Category
    df['revenue_category'] = pd.cut(
        df['Total_Amount'],
        bins=[0, 1000, 5000, 20000, float('inf')],
        labels=['Low', 'Medium', 'High', 'Premium']
    )

    # Weekend flag
    df['weekday'] = df['Date'].dt.day_name()
    df['is_weekend'] = df['Date'].dt.dayofweek >= 5

    # Order Success
    df['order_success'] = (df['Order_Status'] == 'Delivered').astype(int)

    # Rating Category
    df['rating_category'] = df['Ratings'].apply(
        lambda x: 'Excellent' if x >= 4.5
        else 'Good' if x >= 3.5
        else 'Average' if x >= 2.5
        else 'Poor'
    )

    # Customer Value Segment
    df['customer_value_segment'] = pd.cut(
        df['Total_Amount'],
        bins=[0, 5000, 20000, 50000, float('inf')],
        labels=['Low Value', 'Medium Value', 'High Value', 'Very High Value']
    )

    print(f"Transformed: {df.shape}")
    print(f"Nulls remaining: {df.isnull().sum().sum()}")
    return df

def load(df):
    print("Step 3: Loading data...")
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save cleaned dataset
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Saved cleaned dataset → {PROCESSED_PATH}")

    # Save tableau ready dataset
    df.to_csv(TABLEAU_PATH, index=False)
    print(f"Saved tableau dataset → {TABLEAU_PATH}")

def run_pipeline():
    print("=" * 50)
    print("  Retail Analytics ETL Pipeline")
    print("  SectionB Group 3")
    print("=" * 50)
    df = extract()
    df = transform(df)
    load(df)
    print("=" * 50)
    print("ETL Pipeline Complete! ✓")
    print("=" * 50)

if __name__ == "__main__":
    run_pipeline()