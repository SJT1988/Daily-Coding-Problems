# Daily Coding Problem: Problem #1782
# 2024-08-11
# Author: Spencer Trumbore

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

# Minimum Broadcast Range"

import random

def main():
    listeners = []
    towers = []
    populate_list(listeners, 4, 5)
    populate_list(towers, 2, 3)
    min_distance = get_min_distance(listeners, towers)

    print("listeners: " + str(listeners))
    print("towers: " + str(towers))
    print("Minimum Broadcast Range: " + str(min_distance))
    return

def get_min_distance(lst_listeners: list[int], lst_towers: list[int]) -> int:
    min_distances = set()
    for i in lst_listeners:
        min_dist = 1000
        for j in lst_towers:
            if abs(i - j) < min_dist:
                min_dist = abs(i - j)
        min_distances.add(min_dist)
    return max(min_distances)

def populate_list(lst: list[int], min_size: int, max_size: int) -> None:
    size = random.randint(min_size, max_size)
    for i in range(size):
        lst.append(random.randint(0,1000))
    lst.sort()

if __name__ == '__main__':
    main()