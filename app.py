
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Load the dataset
data_path = "used_cars_data.csv"  # Ensure this file is in the correct location
df = pd.read_csv(data_path)

@app.route('/')
def home():
    # Generate a visualization
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price'].dropna(), kde=True, color='blue', bins=30)
    plt.title("Price Distribution")
    plt.xlabel("Price (in Lakhs)")
    plt.ylabel("Frequency")

    # Save the visualization to a file
    viz_path = "static/price_distribution.png"
    plt.savefig(viz_path)
    plt.close()

    # Pass the path to the template
    return render_template("index.html", viz_path=viz_path)

if __name__ == '__main__':
    app.run(debug=True)
