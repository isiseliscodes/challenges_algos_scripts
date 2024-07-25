import redis

# Connect to Redis server
r = redis.Redis()

# Example using SETEX for temporary data (key expires in 10 seconds)
r.setex('greeting', 10, 'Hello from Redis!')
print(f"Greeting message set (may not be retrievable after 10 seconds):")  
# This line won't show the value due to potential expiration

# Example using INCR for a counter
visit_count_key = 'website_visits'
r.incr(visit_count_key)  # Increment website visit count by 1
visit_count = int(r.get(visit_count_key))
print(f"Website visits: {visit_count}")  
# Output: Website visits: 1 (assuming no prior visits)

# Example using LPUSH and LRANGE for lists
shopping_list = 'groceries'
r.lpush(shopping_list, 'bread')
r.lpush(shopping_list, 'milk')
r.lpush(shopping_list, 'eggs')
items = r.lrange(shopping_list, 0, 2)  # Get first 3 items
print(f"First 3 items on shopping list: {items}")  
# Output: First 3 items on shopping list: ['eggs', 'milk', 'bread'] (since LPUSH adds to the front)

# Example using SADD and SMEMBERS for SETS
fruits = 'basket'
r.sadd(fruits, 'apple')
r.sadd(fruits, 'banana')
r.sadd(fruits, 'orange')  # Sets automatically remove duplicates
all_fruits = r.smembers(fruits)
print(f"Fruits in the basket: {all_fruits}")  
# Output: Fruits in the basket: {'apple', 'banana', 'orange'} (order may vary for sets)

# Example using ZADD and ZRANGEBYSCORE for sorted sets
players = 'scores'
r.zadd(players, {'Alice': 100, 'Bob': 80, 'Charlie': 95})  # Add players with scores
top_scorers = r.zrangebyscore(players, 90, 100)  # Get players with scores between 90-100
print(f"Top scorers: {top_scorers}")  # Output: Top scorers: ['Alice'] (assuming no other players have scores between 90-100)

# Close connection (optional)
r.close()