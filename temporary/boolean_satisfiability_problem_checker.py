#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Python SAT Problem checker.

the goal of reading SAT Problem File in the CNF DIMACS file
format, and evaluate how many clauses it satisfies given a
solution file.

The SAT Problem File:
    An SAT problem comprises 2 components: Variables and clauses, and the
    CNF DIMACS format was created as a way of defining Boolean expressions
    written in conjunctive normal form.

    ../data/SAT_Problem.txt
    c cnf comment line -> c provides a comment line
    p cnf 6 4 -> p means problem line, general pattern is p FORMAT VARIABLES CLAUSES
    1 -5 3 0
    -2 4 5 0
    4 -6 0
    3 0

    based on the file above, the boolean expression is:
    ( (x1) OR NOT(x5) OR (x3) OR (x4) )
    AND
    ( NOT(x2) OR (x4) OR (x5) )
    AND
    ( (x4) OR NOT(x6) )
    AND
    (x3)

    ----

    ../data/SAT_Solution.txt
    c cnf solution file comment
    v  -1 2 3 4 -5 -6
    v  0    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Original source:
    https://iamkel.dev/sat-problem-checker/
"""

from io import TextIOWrapper
import re

def read_clauses(rel_path_to_problem_file: str) -> list:
    """The function that reads the Problem file to break it down and extract all of its clauses.

    This function is key since it reads the problem file and parses it so all the clauses get
    extracted and added into a list. The function then returns a list where each element is a clause.

    Args:
        rel_path_to_problem_file (str): Relative path to the input file.

    Returns:
        list: Return a list where each element is a clause.
    """
    clauses: list = []

    try:
        file: TextIOWrapper = open(rel_path_to_problem_file,"r")
        clauses_lines = False
        for line in file:
            if line.startswith("p"):
                clauses_lines = True
                continue

            if line.startswith("%"):
                clauses_lines = False

            if clauses_lines:                    
                # removing trailing spaces, removing last 0 items and converting to number
                clause = [int(s) for s in re.split('[\s]+',line.strip())][:-1] 
                clauses.append(clause)            
        file.close()       

    except IOError:
        print("Can not find input file or read data")
        exit()

    return clauses

def read_solution(rel_path_to_solution_file: str) -> list:
    """The function that reads the Problem file to break it down and extract all of its clauses.

    The read_solution function has similar functionality to the read_clauses function previously shown,
    the difference being that the read_solution parses the solution file and returns a list with all
    variables with their corresponding value.

    Args:
        rel_path_to_solution_file (str): Relative path to the input file.

    Returns:
        list: Return a list where each element is a clause as a solution.
    """    
    solution = []

    try:
        file = open(rel_path_to_solution_file,"r")
        for line in file:
            if line.startswith("v"):
                split_solution = line[3:].split(" ")
                for i in range(len(split_solution)):
                    solution.append(split_solution[i])

        # converting list to int and removing last item "0"
        solution = list(map(int, solution))[:-1]
        file.close()       

    except IOError:
        print("Can not find input file or read data")
        exit()

    return solution

def check_satisfation(clauses: list, solution: list) -> None:
    """The function that reads the Problem file to break it down and extract all of its clauses.

    First, note that our function expects 2 parameters: [clauses, solution].
    The clauses parameter is a list of clauses and their variables, which is what the read_solution()
    function returns.
    The solution parameter is a list of variables that represents an attempt to solve the problem. This
    is what the read_solution() function returns.
    Our function iterates over all clauses, evaluating whether any variable in the clause evaluates to
    True, that serves as proof that it satisfies the clause.
    Once all clauses evaluate, the program displays the summary on the console. Quite simple, is it not?
    
    Args:
        clauses (list): Relative path to the input file.
        solution (list): Relative path to the input file.

    Returns:
        None: Print out results.
    """    
    total_clauses = len(clauses)
    total_satistied = 0
    total_non_satisfied = 0

    for i in range(len(clauses)):
        
        satistied = False

        for j in range(len(clauses[i])):
                
            if clauses[i][j] in solution:
                satistied = True
        
        if satistied:
            total_satistied += 1
        else:
            total_non_satisfied += 1    
    
    print("Total Clauses: " + str(total_clauses))
    print("Satisfied Clauses: " + str(total_satistied))
    print("Non Satisfied Clauses: " + str(total_non_satisfied))

def main():
    """Driver code
    """
    # modules/boolean_satisfiability_problem_checker.py
    clauses = read_clauses("data/SAT_Problem.txt")
    solution = read_solution("data/SAT_Solution.txt")
    check_satisfation(clauses,solution)
