#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""The Knapsack problem.

What is the 0/1 Knapsack Problem? We are given N items where each
item has some weight and profit associated with it. We are also given
a bag with capacity W, [i.e., the bag can hold at most W weight in it].
The target is to put the items into the bag such that the sum of
profits associated with them is the maximum possible.

Note: The constraint here is we can either put an item completely into
the bag or cannot put it at all [It is not possible to put a part of
an item into the bag].

Examples:
Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal
to 4. If we select the item with weight 4, the possible profit is 1. And
if we select the item with weight 1, the possible profit is 3. So the
maximum possible profit is 3. Note that we cannot put both the items
with weight 4 and 1 together as the capacity of the bag is 4.

Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/     
"""
 
def knap_sack(W: int, wt: list, val: list, n: int):
    """Naive knapsack recurisve implementation of
    0-1 Knapsack problem.

    Returns the maximum value that can be put in a knapsack of
    capacity W.

    Knapsack Problem using recursion:
    ---------------------------------
    To solve the problem follow the below idea:

    A simple solution is to consider all subsets of items and calculate the total weight and
    profit of all subsets. Consider the only subsets whose total weight is smaller than W.
    From all such subsets, pick the subset with maximum profit.

    Optimal Substructure: To consider all subsets of items, there can be two cases for every item. 

    Case 1: The item is included in the optimal subset.
    Case 2: The item is not included in the optimal set.
    Follow the below steps to solve the problem:

    The maximum value obtained from 'N' items is the max of the following two values. 

    Maximum value obtained by N-1 items and W weight (excluding nth item)
    Value of nth item plus maximum value obtained by N-1 items and (W - weight of the Nth item) [including Nth item].
    If the weight of the 'Nth' item is greater than 'W', then the Nth item cannot be included and Case 1 is the only possibility.

    Args:
        W (int): Maximum weight the bag can hold.
        wt (list): Weight o fall subsets.
        val (list): Maximum possible profit.
        n (int): Number of items the bag can hold.

    Returns:
        function: Return debugger function.
    """
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knap_sack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knap_sack(
                W-wt[n-1], wt, val, n-1),
            knap_sack(W, wt, val, n-1))

def main():
    """Driver code
    """
    # modules/boolean_satisfiability_problem_checker.py
    clauses = read_clauses("data/SAT_Problem.txt")
    solution = read_solution("data/SAT_Solution.txt")
    check_satisfation(clauses,solution)

    # modules/call_by_ref_and_call_by_value.py
    # call by value
    value_1: str = "This is a Teststring"
    call_by_value(value_1)
    print(f"Outside {call_by_value.__name__} function: {value_1}")
    # call by reference
    list_1 = [10,20,30,40]
    call_by_reference(list_1)
    print(f"Outside {call_by_reference.__name__} function: {list_1}")

    # modules/closure.py
    outer_function("Hello World!")

    # modules/decorators.py
    calculate_sum(2,2,4)

    # modules/func_attrib.py
    print(dir(grow_list)) # return all function attributes
    print(grow_list.__name__) # return function name
    print(grow_list.__doc__) # return function docstring
    print(grow_list.__defaults__) # return all default values of function parameters    
    print(grow_list.__code__.co_argcount) # return number of arguments
    print(grow_list.__code__.co_varnames) # return all paramter names

    # modules/has_table.py

    # modules/keywordd_arguments.py
    my_function_1(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    my_function_2(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    my_function_3(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    list_x = [-3, -2, -1, 1, 2, 3]
    list_y = [9, 4, 1, 1, 4, 9]
    plot_my_lists(list_x, list_y, c='red')    

    # modules/knapsack_problem.py
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knap_sack(W, weight, profit, n))   