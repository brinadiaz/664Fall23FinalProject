import pandas as pd
import re

# Load the CSV file into a DataFrame
df = pd.read_csv('yelp_results.csv')  # Replace 'your_file.csv' with the actual file name

# Function to clean and format the address
def clean_address(address):
    # Add your cleaning logic here
    address = address.lower()  # Convert to lowercase
    address = re.sub(r'\s+', ' ', address)  # Remove extra whitespaces
    # Add more cleaning steps as needed

    # Format the address as specified
    formatted_address = ' '.join(address.split())
    return formatted_address

# Apply the clean_address function to the 'address' column and create a new column 'cleaned_address'
df['cleaned_address'] = df['Address'].apply(clean_address)

# Display the DataFrame with the new column
print(df)

# Save the DataFrame with the cleaned data to a new CSV file
df.to_csv('cleaned_addresses.csv', index=False)  # Replace 'cleaned_addresses.csv' with the desired output file name
