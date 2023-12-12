import pandas as pd

# Assuming merged_df is your DataFrame resulting from merging two CSV files
# Replace this with your actual DataFrame
merged_df = pd.read_csv('output_matching_addresses.csv')

# Sort the DataFrame based on the 'Address' column in a case-insensitive manner
sorted_df = merged_df.sort_values(by='Address', key=lambda x: x.str.lower())

# Replace 'output_sorted_addresses.csv' with your desired output file name
output_file_path = 'output_sorted_addresses.csv'

# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv(output_file_path, index=False)

print(f"The sorted DataFrame has been successfully written to {output_file_path}")
