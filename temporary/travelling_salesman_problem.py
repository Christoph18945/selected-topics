# Python3 program to implement traveling salesman
# problem using naive approach.

"""Travelling Salesman problem.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/
"""

from sys import maxsize
from itertools import permutations

V = 4

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






    # modules/tsp.py
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travelling_salesman_problem(graph, s))

    # classes/Singleton.py
    x = OnlyOne('sausage')
    print(x)
    y = OnlyOne('eggs')
    print(y)
    z = OnlyOne('spam')
    print(z)
    print(x)
    print(y)
    print('x')
    print('y') 
    print('z') 
    output = '''
    <__main__.__OnlyOne instance at 0076B7AC>sausage
    <__main__.__OnlyOne instance at 0076B7AC>eggs
    <__main__.__OnlyOne instance at 0076B7AC>spam
    <__main__.__OnlyOne instance at 0076B7AC>spam
    <__main__.__OnlyOne instance at 0076B7AC>spam
    <__main__.OnlyOne instance at 0076C54C>
    <__main__.OnlyOne instance at 0076DAAC>
    <__main__.OnlyOne instance at 0076AA3C>
    '''
    print(output)

    x = Singleton('sausage')
    print(x)
    y = Singleton('eggs')
    print(y)
    z = Singleton('spam')
    print(z)
    print(x)
    print(y)
    print('x')
    print('y') 
    print('z') 
    output = '''
    sausage
    eggs
    spam
    spam
    spam
    <__main__.Singleton instance at 0079EF2C>
    <__main__.Singleton instance at 0079E10C>
    <__main__.Singleton instance at 00798F9C>
    '''       

    class foo: pass
    foo = SingletonDecorator(foo)
    x=foo()
    y=foo()
    z=foo()
    x.val = 'sausage'
    y.val = 'eggs'
    z.val = 'spam'
    print(x.val)
    print(y.val)
    print(z.val)
    print(x, y, z)

    x=bar('sausage')
    y=bar('eggs')
    z=bar('spam')
    print(x)
    print(y)
    print(z)
    print(x, y, z)