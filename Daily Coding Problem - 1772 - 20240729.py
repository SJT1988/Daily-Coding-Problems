# Daily Coding Problem: Problem #1772 [Medium]
# 2024-07-29
# Author: Spencer Trumbore

'''
Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.
On the ith jump, you may move exactly i places to the left or right.
Find a path with the fewest number of jumps required to get from 0 to N.
'''

import random

def main():
    '''Driver function.'''

    sequence = []

    n = random.randint(0,100)
    computeJumpSequence(n, sequence)
    printResult(n, sequence)

def computeJumpSequence(n: int, sequence: list[int]):
    '''Calculutes the sequence of numbers traversed while \"jumping\" from 0 to n.'''
    
    num_jumps = 0
    jump_size = 0
    i = 0
    
    while i <= n:
        sequence.append(i)      
        if (i == n):
            return num_jumps
        
        else:
            jump_size += 1

            if (i + (jump_size) <= n):
                i = i + jump_size

            else:
                i = i - jump_size
            
            num_jumps += 1

def printResult(n: int, sequence: list[int]):
    '''Prints n, the sequence, and the number of \"jumps\" in that sequence.'''

    print("n: " + str(n))    

    seq = ""
    for num in sequence: seq += str(num) + " "
    print("Sequence: " + seq)

    print("Number of Jumps: " + str(len(sequence)-1))

if __name__ == '__main__':
    main()