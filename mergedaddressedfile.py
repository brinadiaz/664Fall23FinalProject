import pandas as pd

# Replace these with the actual file paths of your CSV files
file1_path = 'cleaned_address4.csv'
file2_path = 'NYC_Restaurant_Inspection_Reviews3.csv'

# Assuming you have already read the dataframes
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Merge df1 and df2 using an outer join
merged_df = pd.merge(df1, df2, on='Address', how='outer')

# Identify rows with matching addresses
matching_addresses = merged_df.dropna(subset=['Address'])

# Replace 'output_matching_addresses.csv' with your desired output file name
output_file_path = 'output_matching_addresses.csv'

# Save the matching addresses to a new CSV file
matching_addresses.to_csv(output_file_path, index=False)

print(f"The matching addresses have been successfully written to {output_file_path}")
