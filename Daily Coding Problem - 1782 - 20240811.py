# Daily Coding Problem: Problem #1782
# 2024-08-11
# Author: Spencer Trumbore

'''
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
'''

# "Sum of Least Number of Squares"

import math

def main():
    num = int(input("type a positive integer: "))
    LSoS_sequence = []
    LSoS(num, LSoS_sequence)
    Print_LSoS(LSoS_sequence)

def LSoS(n: int, seq: list[int]):
    if n <= 0:
        print("n must be a positive integer. Canceling.")
        return
    floored_int = math.floor(math.sqrt(n))
    seq.append(floored_int)
    difference = n - math.pow(floored_int,2)
    if (difference > 0):
        LSoS(difference, seq)
    return

def Print_LSoS(seq: list[int]):
    if (not seq):
        return
    stringy_list = ""
    for i in range(0,len(seq)):
        stringy_list += str(seq[i]) + "^2 "
        if i != len(seq) - 1:
            stringy_list += " + "
    print("n = " + stringy_list)
        
if __name__ == '__main__':
    main()