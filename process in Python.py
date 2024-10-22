import os
import multiprocessing


def print_numbers(n):
    for i in range(n + 1):
        print(i)


def secondary(name, number):
    
    print("the name is " + name) 
    print("The secondary PID is " + str(os.getpid()) + " and secondary parent PID is " + str(os.getppid()))
    print_numbers(number)


def main():
    user_input = int(input("Enter a number: "))
    print("The main PID is " + str(os.getpid()) + " and main parent PID is " + str(os.getppid()))
    process = multiprocessing.Process(target=secondary, args=("yakir", user_input))
    process.start()
    process.join()


if __name__ == "__main__":
    main()

