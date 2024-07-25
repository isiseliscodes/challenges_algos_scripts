import threading
import random
import time

# Shared resource (refrigerator) with a lock to prevent race conditions
fridge_lock = threading.Lock()
fridge_content = []


def chef(name):
    global fridge_content

    while True:
        # Chef prepares a dish with a random name
        dish_name = f"Chef {name}'s Special - {random.randint(100, 999)}"

        # Acquire lock to access shared fridge resource
        with fridge_lock:
            # Add dish to fridge
            fridge_content.append(dish_name)
            print(f"Chef {name} cooked {dish_name} and placed it in the fridge.")

            # Simulate some time to prepare another dish
            time.sleep(2)


def eater(name):
    global fridge_content

    while True:
        # Check if fridge is empty before acquiring lock
        if not fridge_content:
            print(f"{name} found the fridge empty. :(")
            time.sleep(1)
            continue

        # Acquire lock to access shared fridge resource
        with fridge_lock:
            # Grab a random dish from the fridge
            eaten_dish = random.choice(fridge_content)
            fridge_content.remove(eaten_dish)
            print(f"{name} happily ate {eaten_dish}.")

            # Simulate some time to eat and potentially come back for more
            time.sleep(randomatic_eating_time())


def randomatic_eating_time():
    # Simulate random eating times between 1 and 4 seconds
    return random.uniform(1, 4)


# Create two chefs and two eaters with different names
chefs = [threading.Thread(target=chef, args=(f"Chef-{i}",)) for i in range(2)]
eaters = [threading.Thread(target=eater, args=(f"Eater-{i}",)) for i in range(2)]

# Start all threads
for thread in chefs + eaters:
    thread.start()

# Let the threads run for a while (adjust as needed)
time.sleep(10)

# Print the final fridge content (may or may not be empty)
print("Final fridge content:", fridge_content)