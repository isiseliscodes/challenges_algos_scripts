import threading
import time

def thread_function(name):
    print("Thread {} starting.".format(name))
    time.sleep(2)  # Simulate some work
    print("Thread {} finished.".format(name))

# Create two threads with different names
thread1 = threading.Thread(target=thread_function, args=("Thread-1",))
thread2 = threading.Thread(target=thread_function, args=("Thread-2",))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before exiting the program
thread1.join()
thread2.join()

print("All threads finished.")



'''
Explanation:

Import threading module: Provides tools for multithreading.
Define a thread function: thread_function() performs the task for each thread.
Create thread objects: Instantiate Thread objects, specifying:
target: function to be executed in the thread.
args: arguments to pass to the function.
Start threads: Call start() to initiate thread execution.
Join threads: Call join() to wait for threads to finish before continuing main execution.
Key Points:

Global Interpreter Lock (GIL): Python's multithreading has limitations due to the GIL, which allows only one thread to execute Python bytecode at a time.
True parallelism: For CPU-bound tasks, consider multiprocessing for true parallelism.
I/O-bound tasks: Threading can still improve performance for I/O-bound tasks, as threads can overlap waiting for I/O operations.
Synchronization: Use locks, mutexes, or semaphores to protect shared resources from race conditions.
Additional Notes:

Use daemon threads for background tasks that don't block program termination.
Explore ThreadPoolExecutor for managing thread pools and efficient task distribution.

'''