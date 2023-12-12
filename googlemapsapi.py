import requests
import csv
import time

def get_google_maps_reviews(api_key, place_id):
    base_url = "https://maps.googleapis.com/maps/api/place/details/json"

    params = {
        'place_id': place_id,
        'fields': 'name,formatted_address,reviews',
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    result = response.json().get('result', {})

    name = result.get('name', 'N/A')
    formatted_address = result.get('formatted_address', 'N/A')
    
    print(f"Name: {name}")
    print(f"Formatted Address: {formatted_address}")

    reviews = result.get('reviews', [])
    return name, formatted_address, reviews

def find_mexican_restaurants(api_key, location, radius=7000, keyword='mexican restaurant', max_results=2000):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    params = {
        'location': location,
        'radius': radius,
        'keyword': keyword,
        'key': api_key
    }

    results = []
    while len(results) < max_results:
        response = requests.get(base_url, params=params)
        data = response.json()
        current_results = data.get('results', [])

        for restaurant in current_results:
            results.append(restaurant)

        next_page_token = data.get('next_page_token')
        if not next_page_token:
            break

        # Wait a short time before making the next request
        time.sleep(0.1)

        params['pagetoken'] = next_page_token

    return results[:max_results]

def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Formatted Address", "Author", "Rating", "Time", "Review"])

        for entry in data:
            writer.writerow(entry)

def main():
    api_key = 'my_api_here'
    
    manhattan_location = '40.7831, -73.9712'
    mexican_restaurants = find_mexican_restaurants(api_key, manhattan_location)

    data_to_write = []

    for restaurant in mexican_restaurants:
        name = restaurant.get('name', 'N/A')
        place_id = restaurant.get('place_id', 'N/A')

        print(f"\nGetting details and reviews for {name}")
        name, formatted_address, reviews = get_google_maps_reviews(api_key, place_id)

        if reviews:
            for review in reviews:
                author_name = review.get('author_name', 'N/A')
                rating = review.get('rating', 'N/A')
                text = review.get('text', 'N/A')
                time = review.get('relative_time_description', 'N/A')

                print(f"Author: {author_name}, Rating: {rating}, Time: {time}")
                print(f"Review: {text}\n")

                data_to_write.append([name, formatted_address, author_name, rating, time, text])
        else:
            print("No reviews available.")

    write_to_csv(data_to_write, 'mexican_restaurant_reviews.csv')

if __name__ == "__main__":
    main()
