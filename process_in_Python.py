import os
import multiprocessing
import time


def print_numbers(n):
    for i in range(n + 1):
        print(i)
        time.sleep(1)


def secondary(name, number):
    print("the name is " + name) 
    print("The secondary PID is " + str(os.getpid()) + " and secondary parent PID is " + str(os.getppid()))
    print_numbers(number)
    time.sleep(1)


def main():
    user_input = int(input("Enter a number: "))
    print("The main PID is " + str(os.getpid()) + " and main parent PID is " + str(os.getppid()))
    process = multiprocessing.Process(target=secondary, args=("yakir", user_input))
    process.start()
    print("between start to join")
    time.sleep(1)
    print("second line")
    print("third line")
    time.sleep(2) 
    print("maccabi tel aviv")
    time.sleep(1)
    process.join()
    print("done")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(end_time - start_time)






