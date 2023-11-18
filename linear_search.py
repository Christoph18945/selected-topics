#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""linear search

If you want to implement Linear Search in python

Linearly search x in arr[]
If x is present then return its location
else return -1

Searching an element in a list/array in python
can be simply done using \'in\' operator
Example:
if x in arr:
    print arr.index(x)
Note that every element in the list is compared ones.

Time complexity
Worst case: O(n) -> n is the size of the list. The element can be the last.
in the list
Best case O(1) -> the element to be found is the first in the list. 

Auxilary space complexity
O(1) because it only ever consumes space for 1 pointer (array) and 4 integers (length,value,location,i).
it only consumes a constant amount of extra space to store variables.
"""

def main() -> None:
    """main function"""
    linear_search([1,2,3,4,5,6,7,8,9], 4)
    return None
 
def linear_search(arr, x):
    """linear search
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    main()
