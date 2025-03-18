import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def load_data(file_path):
    """Loads CSV or Excel file."""
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        else:
            print("Unsupported file format. Use .csv or .xlsx")
            sys.exit(1)
        return data
    except Exception as e:
        print("Error loading file:", e)
        sys.exit(1)

def basic_analysis(data):
    """Prints basic statistical details."""
    print("\nFirst 5 Rows of Data:")
    print(data.head())
    print("\nBasic Statistics:")
    print(data.describe())
    print("\nMissing Values:")
    print(data.isnull().sum())

def plot_histograms(data):
    """Generates histograms for numerical columns."""
    num_cols = data.select_dtypes(include=['number']).columns
    data[num_cols].hist(figsize=(12, 8), bins=30)
    plt.suptitle("Histograms of Numerical Columns")
    plt.show(block=False)

def plot_correlation_heatmap(data):
    """Generates a correlation heatmap."""
    num_cols = data.select_dtypes(include=['number'])
    plt.figure(figsize=(10, 6))
    sns.heatmap(num_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show(block=False)

def plot_pairplot(data):
    """Generates a pair plot for numeric columns without creating an extra empty figure."""
    num_cols = data.select_dtypes(include=['number'])
    sns.pairplot(num_cols)
    plt.suptitle("Pair Plot of Numeric Features", y=1.02)
    plt.show(block=False)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    data = load_data(file_path)
    basic_analysis(data)
    plot_histograms(data)
    plot_correlation_heatmap(data)
    plot_pairplot(data)
    plt.show()  # Ensure all figures display together

if __name__ == "__main__":
    main()
