#!/usr/bin/env python
import sys


def continue_input():
    while True:
        line = raw_input("please input:")
        if line == "end":
            print "over"
            break
        else:
            print "continue..."


def countdown(n):
    while n != 10:
        if n > 10:
            print n
            n = n - 1
        else:
            print n
            n = n + 1
    print "n is 10 now"


def sequence(n):
    while n != 1:
        print n
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1


def compare(a, b):
    print "aaa" if a > b else "bbb"


def loopString(strin):
    for c in strin:
        print c

    i = 0
    while i < len(strin):
        print strin[i]
        i = i + 1
    print "{0}-{1}".format(9, 'world')

if __name__ == '__main__':
    argv = sys.argv
    # compare(argv[1], argv[2])
    # var = raw_input("Please enter a number: ")
    # countdown(int(var))
    # sequence(int(var))
    # continue_input()
    # print argv
    loopString(argv[1])
