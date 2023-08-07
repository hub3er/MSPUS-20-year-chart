import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(filename):
    # Load the dataset from the CSV file
    df = pd.read_csv(filename)
    return df

def plot_demand_data(df):
    # Convert 'date' column to datetime format
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Plot the 'date' and 'MSPus' columns
    plt.figure(figsize=(12, 6))
    plt.plot(df['DATE'], df['MSPUS'], marker='o', linestyle='-', color='b')
    plt.xlabel('DATE')
    plt.ylabel('Median Sales Price of Houses Sold in US$')
    plt.title('Demand Data: MSPUS over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Provide the filename or file path of the CSV dataset
    dataset_filename = "filename.csv"

    try:
        # Load the dataset
        df = load_dataset(dataset_filename)

        # Plot the demand data
        plot_demand_data(df)

    except FileNotFoundError:
        print(f"File '{dataset_filename}' not found. Please check the file path.")
    except Exception as e:
        print(f"Error: {e}")
