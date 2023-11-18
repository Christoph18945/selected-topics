#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""binary search

Time complexity
Worst case is O(LogN) because the comparison is reached
to reach the first element.

Auxilary space complexity
Binary Search Algorithm uses no extra space to search the element. Hence its auxiliary space complexity is O(1)
"""

def main() -> None:
    """main function"""
    binary_search([2,3,4,10,40], 0, len([2,3,4,10,40])-1, 10)
    return None

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
