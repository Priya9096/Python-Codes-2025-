import threading
import time

def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=background_task)
thread.daemon = True  # Set the thread as a daemon
thread.start()

# Main program ends here
time.sleep(3)
print("Main program ends.")