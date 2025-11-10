import pandas as pd

def analyze_data(file_path):
    """
    Analyzes the data from a CSV file and returns basic statistics.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    dict: A dictionary containing basic statistics of the data.
    """
    # Load the data
    data = pd.read_csv(file_path)

    # Clean data
    data = data.dropna()
    
    #remove duplicates
    data = data.drop_duplicates()

    # check data types
    data = data.convert_dtypes()

    # save updated csv
    data.to_csv('cleaned_data.csv', index=False)

    print(data.head())