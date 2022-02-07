# CodingGears.io
# input & output

import sys


# TODO: Using sys.stdin
def sys_stdin_demo():
    for user_input in sys.stdin:
        if user_input.strip() == "q":
            print("You are quitting now!")
            break
        print("You have entered : {}".format(user_input))


# TODO: using sys.out
def sys_out_demo():
    sys.stdout.write("1: Welcome to CodingGears.io\n")
    print("2: Welcome to CodingGears.io\n")
    sys.stdout = open("console_output.txt", "w")
    print("3: Welcome to CodingGears.io\n")
    sys.stdout = sys.__stdout__
    print("4: Welcome to CodingGears.io\n")


def adhoc():
    name = input("What is your name? ")
    print("Welcome {}".format(name))


if __name__ == '__main__':
    adhoc()
