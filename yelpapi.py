import requests
import csv

api_key = 'TAP6v20ORYrKSoktnVNskhKTfGyLIC6GAamCt4WKEEyuC_RzIR4w04cuT-ZWRf7a11nkbsGGOJJ75FkTeAeqkY0IA72ykdU8vcFZps39ildm7FH4aAzptaU03rNKZXYx'

api_url = 'https://api.yelp.com/v3/businesses/search'
headers = {
    'Authorization': f'Bearer {api_key}',
}

def process_results(offset, businesses, csv_writer):
    for i, business in enumerate(businesses):
        row = [
            offset + i + 1,
            business['name'],
            business['rating'],
            ', '.join(business['location']['display_address']),
            business['phone'],
            business.get('price', 'N/A'),
            ', '.join([c['title'] for c in business['categories']])
        ]
        csv_writer.writerow(row)
        print(f"#{offset + i + 1} - Name: {business['name']}")
        print(f"Rating: {business['rating']}")
        print(f"Address: {', '.join(business['location']['display_address'])}")
        print(f"Phone: {business['phone']}")
        print(f"Price: {business.get('price', 'N/A')}")
        print(f"Categories: {', '.join([c['title'] for c in business['categories']])}")
        print("\n")

# Create a CSV file and write the header
csv_file_path = 'yelp_results.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['#', 'Name', 'Rating', 'Address', 'Phone', 'Price', 'Categories'])

    for iteration in range(0, 3):
        limit = 50
        offset = limit * iteration
        params = {
            'term': 'Mexican',
            'location': 'New York',
            'sort_by': 'rating',
            'limit': limit,
            'offset': offset,
        }

        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            total_results = data['total']
            process_results(offset, data['businesses'], csv_writer)

print(f"Results saved to {csv_file_path}")
