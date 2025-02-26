''' data_preprocessing.py - Cleaning the sales data '''
import pandas as pd
from data_collection import load_data  # Import load_data function

def clean_data(file_path):
    """Loads and cleans the sales data by handling missing values and duplicates."""
    df = load_data(file_path)  # Load the data first
    df.drop_duplicates(inplace=True)  # Remove duplicate rows
    df.dropna(inplace=True)  # Remove missing values
    return df  # Return cleaned DataFrame

if __name__ == "__main__":
    file_path = r"C:\Users\Dell\Desktop\sales data anlaysis\sales_data.csv"
    cleaned_df = clean_data(file_path)
    print("Data Cleaned Successfully!\n", cleaned_df.head())
