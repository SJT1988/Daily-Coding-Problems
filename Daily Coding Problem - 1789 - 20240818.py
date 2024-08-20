# Daily Coding Problem: Problem #1789
# 2024-08-18
# Author: Spencer Trumbore

# "Listeners and Towers Problem"

'''
You are the technical director of WSPT radio, serving listeners nationwide.
For simplicity's sake we can consider each listener to live along a horizontal
line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers, each placed at various
locations along this line, determine what the minimum broadcast range would have
to be in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15].
In this case the minimum range would be 5, since that would be required for
the tower at position 15 to reach the listener at position 20.
'''

# note: This solution requires sorted lists of listeners and towers.
# credit to Pavan Kumar Mungara for this optimized strategy O(m+n)

import random
import sys

def main():
    listeners = []
    towers = []
    populate_list(listeners,5,6)
    populate_list(towers,2,4)
    maxRange = find_max_range(listeners, towers)

    print("listeners: " + str(listeners))
    print("towers: " + str(towers))
    print("Max Range: " + str(maxRange))

def populate_list(lst: list[int], min_size: int, max_size: int) -> None:
    size = random.randint(min_size, max_size)
    for i in range(size):
        lst.append(random.randint(0,100))
    lst.sort()

def find_max_range(listeners: list[int], towers: list[int]) -> int:
    m = len(listeners)
    n = len(towers)
    towerL = 1-sys.maxsize
    towerR = towers[0]
    i,j = 0,0 # listener index, tower index
    distMax = 0

    while (i < m):
        if (listeners[i] < towerR):
            distL = listeners[i] - towerL
            distR = towerR - listeners[i]
            distMin = distL if distL < distR else distR
            if (distMin > distMax):
                distMax = distMin
            i+=1
        else:
            # increment tower indices
            towerL = towers[j]
            if (j < n-1):
                j+=1
                towerR = towers[j]
            else:
                towerR = sys.maxsize
    return distMax

if __name__ == '__main__':
    main()
