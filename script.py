# ============================
# Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib
# Dataset: Iris dataset from sklearn.datasets
# ============================

# ---- Task 1: Load and Explore the Dataset ----
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame  # pandas DataFrame
df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # add species column

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Clean dataset (no missing values in iris, but we demonstrate handling)
df = df.dropna()

# ---- Task 2: Basic Data Analysis ----
print("\nBasic Statistics:")
print(df.describe())

# Grouping: average measurements per species
group_means = df.groupby('species').mean()
print("\nAverage measurements per species:")
print(group_means)

# Observations
print("\nObservations:")
print("- Iris-setosa tends to have the smallest petal length and width.")
print("- Iris-virginica tends to have the largest petal measurements.")
print("- Sepal length varies less across species compared to petal length.")

# ---- Task 3: Data Visualization ----

plt.style.use("seaborn-v0_8")  # nicer plots

# 1. Line chart (trend of sepal length across samples)
plt.figure(figsize=(8,5))
plt.plot(df['sepal length (cm)'], label="Sepal Length")
plt.title("Line Chart: Sepal Length across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
group_means['petal length (cm)'].plot(kind='bar', color=['coral','skyblue','green'])
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=20, color="purple", alpha=0.7)
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (Sepal Length vs Petal Length)
plt.figure(figsize=(8,5))
for species, color in zip(iris.target_names, ["red","blue","green"]):
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['petal length (cm)'], label=species, alpha=0.7, color=color)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

print("\nAnalysis complete.")
