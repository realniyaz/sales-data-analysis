''' data_transformation.py - Transforming the sales data '''
import pandas as pd
from data_preprocessing import clean_data  # Import cleaning function

def transform_data(file_path):
    """Loads, cleans, and transforms the sales data."""
    df = clean_data(file_path)  # Ensure df is a DataFrame
    df['Date'] = pd.to_datetime(df['Date'])  # Convert Date column to datetime
    category_revenue = df.groupby("Category")["Revenue"].sum().reset_index()  # Aggregate revenue by category
    return category_revenue

if __name__ == "__main__":
    file_path = r"C:\Users\Dell\Desktop\sales data anlaysis\sales_data.csv"
    transformed_df = transform_data(file_path)
    print("Data Transformed Successfully!\n", transformed_df)
