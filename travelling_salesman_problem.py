#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Travelling Salesman problem.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/
"""

from sys import maxsize
from itertools import permutations

V = 4

def main() -> None:
    """main function"""
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travelling_salesman_problem(graph, s))
    return None

def travelling_salesman_problem(graph: list[list], s: int):
    """Implementation of traveling Salesman Problem.

    Args:
        graph (Any): .
        s (Any): .

    Returns:
        int: Prints out results.
    """ 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        # update minimum
        min_path = min(min_path, current_pathweight)
         
    return min_path

if __name__ == "__main__":
    main()
 