import pandas as pd
from fuzzywuzzy import process

def find_similar_entries(df1, df2, df3, address_column_name, threshold=150):
    similar_entries = []

    # Read data from CSV files
    df1 = pd.read_csv(df1)
    df2 = pd.read_csv(df2)
    df3 = pd.read_csv(df3)

    # Fuzzy match for the 'address' column name
    match1, _ = process.extractOne('address', df1.columns)
    match2, _ = process.extractOne('address', df2.columns)
    match3, _ = process.extractOne('address', df3.columns)

    # Merge dataframes using the fuzzy matched 'address' column names
    merged_df = pd.merge(df1, df2, left_on=match1, right_on=match2, how='inner')
    merged_df = pd.merge(merged_df, df3, left_on=match1, right_on=match3, how='inner')

    for col1 in merged_df.columns:
        for index1, row1 in merged_df.iterrows():
            value1 = row1[col1]

            for col2 in df2.columns:
                # Skip columns in df2 that have more than two values
                if len(df2[col2].unique()) != 2:
                    print(f"Skipping col2: {col2}, values: {df2[col2].unique()}")
                    continue

                try:
                    match2, score2 = process.extractOne(value1, df2[col2])
                except ValueError as e:
                    print(f"Error in col2: {col2}, value1: {value1}, Exception: {e}")
                    continue

                for col3 in df3.columns:
                    match3, score3 = process.extractOne(value1, df3[col3])

                    if score2 >= threshold and score3 >= threshold:
                        similar_entries.append((col1, value1, col2, match2, score2, col3, match3, score3))

    return similar_entries

file1_path = 'cleaned_addresses3.csv'
file2_path = 'NYC_Restaurant_Inspection_Results2.csv'
file3_path = 'mexican_restaurant_reviews2.csv'

similarity_threshold = 150

similar_entries = find_similar_entries(file1_path, file2_path, file3_path, 'address', similarity_threshold)

columns = ['col1', 'value1', 'col2', 'match2', 'score2', 'col3', 'match3', 'score3']
results_df = pd.DataFrame(similar_entries, columns=columns)

results_df.to_csv('similar_entries_results.csv', index=False)
