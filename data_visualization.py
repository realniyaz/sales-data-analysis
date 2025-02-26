''' data_visualization.py - Visualizing the sales data '''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_transformation import transform_data  # Import transformed data function

def visualize_data(file_path):
    """Loads, transforms, and visualizes the sales data."""
    df = transform_data(file_path)  # Get transformed data
    
    # Bar plot for revenue by category
    plt.figure(figsize=(8, 5))
    sns.barplot(x="Category", y="Revenue", data=df, palette="viridis")
    plt.xlabel("Product Category")
    plt.ylabel("Total Revenue")
    plt.title("Total Revenue by Category")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    file_path = r"C:\Users\Dell\Desktop\sales data anlaysis\sales_data.csv"
    visualize_data(file_path)
