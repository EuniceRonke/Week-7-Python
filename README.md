# Analyzing Data with Pandas and Visualizing Results with Matplotlib

## Overview
This project analyzes the famous **Iris dataset** using `pandas` for data exploration and `matplotlib` for visualizations.  
It demonstrates how to load, clean, analyze, and visualize data in Python.

---

## Objectives
- Load and explore a dataset using **pandas**
- Perform basic statistical analysis
- Group data and compute aggregated values
- Visualize results with **Matplotlib**

---

## Dataset
The dataset used is the **Iris dataset**, available directly from `sklearn.datasets.load_iris()`.  
It contains 150 samples of iris flowers with 4 numerical features:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

Each flower belongs to one of three species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

---

## Project Tasks

### 1. Load and Explore the Dataset
- Import the Iris dataset from `sklearn.datasets`
- Convert to a pandas DataFrame
- Inspect the first 5 rows
- Check data types, shape, and missing values

### 2. Basic Data Analysis
- Compute descriptive statistics (`mean`, `std`, `min`, `max`)
- Group data by species and calculate average values
- Identify interesting observations and patterns

### 3. Data Visualizations
Created using **Matplotlib**:
1. **Line Chart** – Sepal length across samples
2. **Bar Chart** – Average petal length per species
3. **Histogram** – Sepal width distribution
4. **Scatter Plot** – Sepal length vs Petal length across species
   
Results & Observations

Iris-setosa has the smallest petals on average

Iris-virginica has the largest petals

Sepal length varies less across species compared to petal length

Clear separation of species is visible in the scatter plot

Requirements

Python 3.x

pandas

matplotlib

scikit-learn

Author

Eunice 
---
