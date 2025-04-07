import time
import threading

def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def print_characters():
    for i in ['A','B','C','D','E']:
        print(i)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_characters)
thread1.start()
thread2.start()

print(f"Is thread1 alive? {thread1.is_alive()}")

thread1.join()
thread2.join()

print(f"Is thread1 alive? {thread1.is_alive()}")

print('All threads executed')


