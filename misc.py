#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Miscellaneous algorithms.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

def main() -> None:
    """driver code"""
    a = 10
    b = 15
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    a = 35
    b = 10
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    a = 31
    b = 2
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    print(fibonacci(9))
    print_pascal(7)
    nums = [-2,1,-3,7,-2,2,1,-5,4]
    ob1 = Solution()
    print(ob1.max_sub_array(nums)) 
    return None  

# Python3 program to demonstrate Basic Euclidean Algorithm
# -------------------------------------------------------- 
# Function to return gcd of a and b
def gcd(a: int, b: int) -> int:
    """Returns gcd of a and b.

    Args:
        a (int): A single value of your choice.
        a (int): A single value of your choice.

    Returns:
        function: Return debugger function.
    """    
    if a == 0:
        return b
    result = b % a

    return gcd(result, a)

def multiply_matrices() -> None:
    """Program to multiply matrices.

    Multiply two matrices using nested loops.

    Args:
        a (int): A single value of your choice.
        a (int): A single value of your choice.

    Returns:
        function: Return debugger function.
    """ 
    # take a 3x3 matrix
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]
    
    # take a 3x4 matrix   
    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
        
    result = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    
    # iterating by row of A
    for i in range(len(A)):
        # iterating by column by B
        for j in range(len(B[0])):
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    for r in result:
        print(r)

    return None


# Function for nth Fibonacci number
# ------------------------------------
def fibonacci(n: int) -> int:
    """Function for nth Fibonacci number.

    Recursive approach.

    Args:
        n (int): Maximum length to calculate fibonacci sequence.

    Returns:
        int: retursn calcualated fibonacci umbers.
    """    
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        print(fibonacci(n-1) + fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)

# pascals triangle
# --------------------------------------------
# Python 3 code for Pascal's Triangle

 
# Function to print
# first n lines of
# Pascal's Triangle
def print_pascal(n) :
    """Pasclas triangle.

    A simple O(n^3) program for Pascal's Triangle.

    Args:
        n (int): Maximum length of Pascals Triangle.

    Returns:
        int: .
    """    
    # Iterate through every line
    # and print entries in it
    for line in range(0, n) :  
        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1) :
            print(binomial_coeff(line, i),
                " ", end = "")
        print()
 
def binomial_coeff(n, k):
    """Binomial Coefficient.

    Details: https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/

    Args:
        n (int): .
        k (int): .

    Returns:
        int: .
    """  
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
     
    return res

class Solution(object):
    """"""
    def __init__(self):
        """class constructor"""
        ...

    def max_sub_array(self, nums):
        """Maximum sub array.

        Args:
            nums (int): .

        Returns:
            int: .        
        """
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

if __name__ == "__main__":
    main()
