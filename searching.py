#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""linear search
"""

# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
#   print arr.index(x)

def main() -> None:
    """main function"""
    linear_search([1,2,3,4,5,6,7,8,9], 4)
    binary_search([2,3,4,10,40], 0, len([2,3,4,10,40])-1, 10)
    return None

# If you want to implement Linear Search in python

# Linearly search x in arr[]
# If x is present then return its location
# else return -1
 
def linear_search(arr, x):
    """linear search
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    """Binary search
    """
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

if __name__ == "__main__":
    main()
