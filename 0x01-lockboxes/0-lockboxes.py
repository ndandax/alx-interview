#!/usr/bin/python3
'''a module to unlock boxes'''


def canUnlockAll(boxes):
    """a function unlock boxes"""
    unlocked = [0]
    for i in unlocked:
        keys = boxes[i]

        for j in keys:
            if j not in unlocked:
                unlocked.append(j)
    return len(unlocked) == len(boxes)
