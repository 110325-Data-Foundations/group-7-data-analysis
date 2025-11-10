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

    # get columns
    columns = data.columns.tolist()
    print(f"Columns in the dataset: {columns}")

    # Clean data
    data = data.dropna()

    # count duplicates for each column
        # count duplicates for each column
    for col in columns:
        col_dup_count = data[col].duplicated().sum()
        print(f"Number of duplicate values in column '{col}': {col_dup_count}")
    
    
    #remove duplicates
    data = data.drop_duplicates()

    # count duplicates after removal
    duplicate_count_after = data.duplicated().sum()
    print(f"Number of duplicate rows after removal: {duplicate_count_after}")

    # check data types
    data = data.convert_dtypes()

    # save updated csv
    data.to_csv('cleaned_data.csv', index=False)

    print(data.head())

analyze_data('dataset.csv')