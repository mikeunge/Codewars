#!/usr/bin/python3
#-*-coding:utf-8-*-


# Check if the sum from arr is even or odd.
def odd_or_even(arr):
    if sum(arr) % 2:
        return "odd"
    return "even"


# Smartest way i found...
def odd_or_even_smart(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


def test():
    print(odd_or_even([0,1,2]))
    print(odd_or_even([0]))
    print(odd_or_even([12,872,43,920,38,4]))
    print(odd_or_even([19,23,4,21,0]))


if __name__ == "__main__":
    test()
