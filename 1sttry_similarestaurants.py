import csv

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        return header

def find_common_columns(file1, file2):
    columns_file1 = set(read_csv(file1))
    columns_file2 = set(read_csv(file2))
    common_columns = columns_file1.intersection(columns_file2)
    return common_columns

def read_csv_with_columns(file_path, columns):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({column: row[column] for column in columns})
    return data

def write_csv(data, output_file, columns):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)

def find_similar_rows(file1, file2, output_file, column_mapping):
    common_columns = set(column_mapping.keys())

    if not common_columns:
        print("Error: No common columns specified.")
        return

    data1 = read_csv_with_columns(file1, common_columns)
    data2 = read_csv_with_columns(file2, common_columns)

    common_rows = []
    for row1 in data1:
        for row2 in data2:
            is_similar = all(row1[col].lower() == row2[column_mapping[col]].lower() for col in common_columns)
            if is_similar:
                common_rows.append(row1)
                break  # Break to avoid adding the same row multiple times

    if common_rows:
        write_csv(common_rows, output_file, common_columns)
        print(f"Similar rows written to {output_file}")
    else:
        print("No similar rows found.")

if __name__ == "__main__":
    # Replace with your file paths and column mappings
    file1_path = 'mexican_restaurant_reviews.csv'
    file2_path = 'Restaurant_Inspection_Results_AB.csv'
    output_file_path = 'similar_rows.csv'
    column_mapping = {'Name': 'NAME', 'NAME': 'Name'}

    find_similar_rows(file1_path, file2_path, output_file_path, column_mapping)
