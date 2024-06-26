import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('You eat breakfast.')
def drink_coffee():
    time.sleep(4)
    print("You drink coffee.")
def study():
    time.sleep(10)
    print("You finish your studies.")

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

# eat_breakfast()
# drink_coffee()
# study()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())