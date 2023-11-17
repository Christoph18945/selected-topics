#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://miro.medium.com/v2/resize:fit:786/format:webp/1*X1hZCxNdfgZ0sT_2tynPKA.png
    https://www.bigocheatsheet.com/
    https://blog.devgenius.io/python-time-complexities-1988ec5d16d9
    https://medium.com/analytics-vidhya/how-to-find-the-time-complexity-of-a-python-code-95b0237e0f2d
    https://www.freecodecamp.org/news/learn-big-o-notation/
"""

import datetime

def main() -> None:
    """main function"""
    # modules/time_complexities.py
    # Constant Time — O(1)
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(get_first(data))
    # Logarithmic Time — O(log n)
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(binary_search(data, 8))
    # Linear Time — O(n)
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(linear_search(data, 7))
    # Quasilinear Time — O(n log n)
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    merge_sort(data)
    print(data)
    # Quadratic Time — O(n²)
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    bubble_sort(data)
    print(data)
    # Exponential Time — O(2^n)
    fibonacci_time_complexity(4)
    # Factorial — O(n!)
    data = [1, 2, 3]
    heap_permutation(data, len(data))
    return None

# Constant Time — O(1)
# --------------------
# An algorithm is said to have a constant time when it is not dependent on the input data (n).
# No matter the size of the input data, the running time will always be the same. For example:
data = [1, 5, 3, 9, 2, 4, 6, 7, 8]
# if a > b:
#     return True
# else:
#     return False

# Now, let’s take a look at the function get_first which returns the first element of a list:
def get_first(data: list) -> int:
    """Return a value of data.

    calcualte time complexity bere
    https://medium.com/analytics-vidhya/how-to-find-the-time-complexity-of-a-python-code-95b0237e0f2d

    Args:
        data (list): List with random data.
        value (): .

    Returns:
        int: Returns a single element of a list.
    """
    start_time = datetime.datetime.now()
    data[0]
    end_time = datetime.datetime.now()
    print( f'Duration: { end_time - start_time }')

    start_time_1 = datetime.datetime.now()
    data[1]
    end_time_1 = datetime.datetime.now()
    print( f'Duration: { end_time_1 - start_time_1 }')

    start_time_2 = datetime.datetime.now()
    data[2]
    end_time_2 = datetime.datetime.now()
    print( f'Duration: { end_time_2 - start_time_2 }')

    start_time_3 = datetime.datetime.now()
    data[3]
    end_time_3 = datetime.datetime.now()
    print( f'Duration: { end_time_3 - start_time_3 }') 

    return data[0]

# Independently of the input data size, it will always have the same running time since it only
# gets the first value from the list. An algorithm with constant time complexity is excellent
# since we don’t need to worry about the input size.


# Linear Time — O(n)
# ------------------
# An algorithm is said to have a linear time complexity when the running time increases at most linearly
# with the size of the input data. This is the best possible time complexity when the algorithm must
# examine all values in the input data. For example:

# Note that in this example, we need to look at all values in the list to find the value we are looking for.

for value in data:
    print(value)

# Let’s take a look at the example of a linear search, where we need to find the position of an element in an unsorted list:

def linear_search(data, value):
    """Calculate the middle of the list..

    Args:
        data (Any): Message as plain text.
        value (): .

    Returns:
        function: Return the inner_function.
    """    
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')


# Logarithmic Time — O(log n)
# ---------------------------
# An algorithm is said to have a logarithmic time complexity when it reduces the size of the input
# data in each step (it don’t need to look at all values of the input data), for example:

for index in range(0, len(data), 3):
    print(data[index])

# Algorithms with logarithmic time complexity are commonly found in operations on binary trees or
# when using binary search. Let’s take a look at the example of a binary search, where we need to
# find the position of an element in a sorted list:

def binary_search(data, value):
    """Calculate the middle of the list..

    Calculate the middle of the list.
    If the searched value is lower than the value in the middle of the list, set a new right bounder.
    If the searched value is higher than the value in the middle of the list, set a new left bounder.
    If the search value is equal to the value in the middle of the list, return the middle (the index).
    Repeat the steps above until the value is found or the left bounder is equal or higher the right bounder.
    It is important to understand that an algorithm that must access all elements of its input data cannot take logarithmic time, as the time taken for reading input of size n is of the order of n.

    Args:
        data (Any): Message as plain text.
        value (): .

    Returns:
        function: Return the inner_function.
    """
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')


# Quasilinear Time — O(n log n)
# -----------------------------
# An algorithm is said to have a quasilinear time complexity when each operation in the input data have
# a logarithm time complexity. It is commonly seen in sorting algorithms (e.g. mergesort, timsort, heapsort).
# For example: for each value in the data1 (O(n)) use the binary search (O(log n)) to search the same
# value in data2.

# for value in data1:
#     result.append(binary_search(data2, value))

# Another, more complex example, can be found in the Mergesort algorithm. Mergesort is an efficient,
# general-purpose, comparison-based sorting algorithm which has quasilinear time complexity,
# let’s see an example:

def merge_sort(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    merge_sort(left_data)
    merge_sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]

# Quadratic Time — O(n²)
# --------------------
# An algorithm is said to have a quadratic time complexity when it needs to perform a linear time
# operation for each value in the input data, for example:

for x in data:
    for y in data:
        print(x, y)

# Bubble sort is a great example of quadratic time complexity since for each value it needs to
# compare to all other values in the list, let’s see an example:

def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True

# Exponential Time — O(2^n)
# -------------------------
# An algorithm is said to have an exponential time complexity when the growth doubles with each addition to
# the input data set. This kind of time complexity is usually seen in brute-force algorithms.

# In cryptography, a brute-force attack may systematically check all possible elements of a password by
# iterating through subsets. Using an exponential algorithm to do this, it becomes incredibly resource-expensive
# to brute-force crack a long password versus a shorter one. This is one reason that a long password is
# considered more secure than a shorter one.

# Another example of an exponential time algorithm is the recursive calculation of Fibonacci numbers:

def fibonacci_time_complexity(n):
    if n <= 1:
        return n
    return fibonacci_time_complexity(n-1) + fibonacci_time_complexity(n-2)

# If you don’t know what a recursive function is, let’s clarify it quickly: a recursive function may be described
# as a function that calls itself in specific conditions. As you may have noticed, the time complexity of recursive
# functions is a little harder to define since it depends on how many times the function is called and the time
# complexity of a single function call.

# It makes more sense when we look at the recursion tree. The following recursion tree was generated by the
# Fibonacci algorithm using n = 4:

# Recursion tree of Fibonacci(4): https://visualgo.net/bn/recursion
# Note that it will call itself until it reaches the leaves. When reaching the leaves it returns the value itself.

# Now, look how the recursion tree grows just increasing the n to 6:

# Recursion tree of Fibonacci(6): https://visualgo.net/bn/recursion
# You can find a more complete explanation about the time complexity of the recursive Fibonacci algorithm here on StackOverflow.

# Factorial — O(n!)
# --------------- 
# An algorithm is said to have a factorial time complexity when it grows in a factorial way based on the size of the input data, for example:

# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 6! = 6 x 5 x 4 x 3 x 2 x 1 = 720
# 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5.040
# 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40.320
# As you may see it grows very fast, even for a small size input.
# 
# A great example of an algorithm which has a factorial time complexity is the Heap’s algorithm, which is used for generating all possible permutations of n objects.
# 
# According to Wikipedia:
# 
# Heap found a systematic method for choosing at each step a pair of elements to switch, in order to produce every possible permutation of these elements exactly once.
# 
# Let’s take a look at the example:

def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]

# The result will be:
# [1, 2, 3]
# [2, 1, 3]
# [3, 1, 2]
# [1, 3, 2]
# [2, 3, 1]
# [3, 2, 1]
# Note that it will grow in a factorial way, based on the size of the input data, so we can say the algorithm has factorial time complexity O(n!).

# Another great example is the Travelling Salesman Problem.

# Important Notes
# It is important to note that when analyzing the time complexity of an algorithm with several operations we need to describe the algorithm based on the largest complexity among all operations. For example:

# def my_function(data):
#     first_element = data[0]
    
#     for value in data:
#         print(value)
    
#     for x in data:
#         for y in data:
#             print(x, y)
# Even that the operations in 'my_function' don’t make sense we can see that it has multiple time complexities: O(1) + O(n) + O(n²). So, when increasing the size of the input data, the bottleneck of this algorithm will be the operation that takes O(n²). Based on this, we can describe the time complexity of this algorithm as O(n²).

if __name__ == "__main__":
    main()
