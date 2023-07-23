#!/usr/bin/python3
import sys
 
if __name__ == "__main__":
    # arguments
    argv = sys.argv

    # total arguments
    n = len(argv) - 1

    if n == 0:
        print("{:d} arguments.".format(n))
    elif n == 1:
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))