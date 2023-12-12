import pandas as pd

def find_overlapping_addresses(file1_path, file2_path):
    # Read CSV files into Pandas DataFrames
    df1 = pd.read_csv(file1_path, encoding='utf-8')
    df2 = pd.read_csv(file2_path, encoding='utf-8')

    # Convert the Address columns to lowercase for case-insensitive comparison
    df1['Address_lower'] = df1['Address'].str.lower()
    df2['Address_lower'] = df2['Address'].str.lower()

    # Find overlapping addresses
    overlapping_addresses = pd.merge(df1, df2, how='inner', left_on='Address_lower', right_on='Address_lower')['Address'].unique()

    # Display or save the result
    if len(overlapping_addresses) > 0:
        print("Overlapping Addresses:")
        for address in overlapping_addresses:
            print(address)
    else:
        print("No overlapping addresses found.")

# Example usage
file1_path = 'cleaned_addresses3.csv'
file2_path = 'NYC_Restaurant_Inspection_Results.csv'
find_overlapping_addresses(file1_path, file2_path)
