# Implementation of binary search algorithm
# We will prove that binary search is faster than naive search!
# Naive search: Can scan an entire list and ask if its equal to the target
# if yes, return the index
# if no, then return 1
import random
import time

"""
The Problem:
Imagine you have a big box of numbered toys, and you want to find a specific toy with a particular number.
You can either look at each toy one by one (like counting from 1 to 10) or use a smarter way to find it quickly.
Naive Search (Looking at Each Toy):
The first method is like checking each toy in order. You start with toy number 1, then 2, then 3, and so on.
If you find the toy with the right number, you say, “I found it!” and show everyone where it is.
But if you don’t find it, you just say, “I couldn’t find it.”
Binary Search (The Clever Way):
The second method is smarter. It’s like playing a guessing game.
You pick a toy from the middle of the box (let’s call it “Toy X”). You look at its number.
If Toy X has the right number, you say, “I found it!” and show everyone.
If Toy X’s number is too big, you know the right toy must be in the first half of the box. So you ignore the other half.
If Toy X’s number is too small, you know the right toy must be in the second half of the box. So you ignore the first half.
Then you repeat the same steps with the remaining half of the toys.
Keep doing this until you find the right toy. It’s like cutting the box in half each time!
"""

def naive_search(l, target):
    # Example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# Binary search uses divide and conquer
# we will leverage the fact that our list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # example l = [1, 3, 5, 10, 12]
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start) / length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")
