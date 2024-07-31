import redis
import json
import time

# Mock database (a dictionary simulating a database)
mock_db = {
    1: {"name": "Pizza Place", "address": "123 Main St", "rating": 4.5},
    2: {"name": "Burger Joint", "address": "456 Elm St", "rating": 4.0},
    3: {"name": "Sushi Spot", "address": "789 Oak St", "rating": 4.7},
}

# Connect to Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def get_restaurant_details(restaurant_id):
    # Check if the restaurant details are in the cache
    cached_data = r.get(f'restaurant:{restaurant_id}')
    
    if cached_data:
        print(f"Cache hit for restaurant ID {restaurant_id}")
        return json.loads(cached_data)
    else:
        print(f"Cache miss for restaurant ID {restaurant_id}")
        # Simulate fetching data from the mock database
        restaurant = mock_db.get(restaurant_id)
        
        if restaurant:
            # Store the restaurant details in the cache with an expiration time of 60 seconds
            r.setex(f'restaurant:{restaurant_id}', 60, json.dumps(restaurant))
            return restaurant
        else:
            return None

# Test the caching logic
if __name__ == '__main__':
    # Fetch restaurant details
    restaurant_id = 1
    restaurant_details = get_restaurant_details(restaurant_id)
    print(f"Restaurant details: {restaurant_details}")

    # Wait for a few seconds and fetch again to see the caching in action
    time.sleep(5)
    restaurant_details = get_restaurant_details(restaurant_id)
    print(f"Restaurant details: {restaurant_details}")

    # Wait for 60 seconds to let the cache expire
    print("Waiting for cache to expire...")
    time.sleep(60)
    restaurant_details = get_restaurant_details(restaurant_id)
    print(f"Restaurant details: {restaurant_details}")
