# Multithreading
import threading

import time

def func1():
    for i in ('asddfghj'):
        print(i)
        time.sleep(2)

def func2():
    for i in range(10):
        print( i**2)
        time.sleep(1)


thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()




def print_kub(num):
	print("kub: {}" .format(num * num * num))


def print_kvadrat(num):
	print("kvadrat: {}" .format(num * num))


if __name__ =="__main__":
	t1 = threading.Thread(target=print_kvadrat, args=(10,))
	t2 = threading.Thread(target=print_kub, args=(10,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()


import threading
import time

def math1():
    for i in range(10):
        if i%2==0:
        	print(i)
       		time.sleep(2)

def math2():
    for i in range(10):
        if i % 2 == 1:
            print(i)
            time.sleep(1)

thread1 = threading.Thread(target=math1)
thread2 = threading.Thread(target=math2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
