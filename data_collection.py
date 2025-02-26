''' data_collection.py - Collecting the sales data '''
import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file into a Pandas DataFrame."""
    df = pd.read_csv(file_path)  # Use the passed file path
    return df

if __name__ == "__main__":
    file_path = r"C:\Users\Dell\Desktop\sales data anlaysis\sales_data.csv"  # Use raw string
    df = load_data(file_path)  # Pass file_path as an argument
    print("Data Loaded Successfully!\n", df.head())

