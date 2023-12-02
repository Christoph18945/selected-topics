#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pathlib import Path
from py2cfg import CFGBuilder
import dis

"""
- CPYTHON INTERNALS
    - 1. Source Compiler: Is the .py file. The file is executed and looks like the following here:
    - 2. Compiler: The code is compiled here
    - 3. AST: Abstract Syntax Tree is interesting here, because you can built linter to check python source code here.
    - 4. Control Flow Graph: Graph shows all 
    - 5. Bytecode: Converted into bytecode. It is a stack of commands
    - 6. Interpreter: Interpreter executes the code then
- BYTECODE
    - 1. line#
    - 2. Offset
    - 3. Operation Name
    - 4. Arg Index
    - 5. Arg Value
"""

def main():
    """main program"""

    # Addendum - 3. AST - Abstract Syntax Tree
    # ----------------------------------------
    # Call here:
    # python3 -m ast python_under_the_hood.py
    # to show the Abstract Syntax Tree in cmdl
    function_1()
    function_2()

    # Addendum - 4. Control Flow Graph
    # ---------------------------------
    # Show the Control Flow graph
    FILEPATH: Path = Path(__file__).parent.joinpath("python_under_the_hood.py")
    FILEPATH = str(FILEPATH)
    cfg = CFGBuilder().build_from_file('python_under_the_hood_CGF', str(FILEPATH))
    cfg.build_visual('python_under_the_hood_CGF','png')

    # Disassemble the python bytecode:
    dis.dis(function_1)
    dis.dis(function_1)
    # The ooutput would be:
    #  75      0 LOAD_CONST               1 ('{} {}')
    #          2 LOAD_METHOD              0 (format)
    #          4 LOAD_CONST               2 ('Christoph')
    #          6 LOAD_CONST               3 ('Hartleb')
    #          8 CALL_METHOD              2
    #         10 RETURN_VALUE
    # 75       0 LOAD_CONST               1 ('{} {}')
    #          2 LOAD_METHOD              0 (format)
    #          4 LOAD_CONST               2 ('Christoph')
    #          6 LOAD_CONST               3 ('Hartleb')
    #          8 CALL_METHOD              2
    #         10 RETURN_VALUE

def function_1():
    return "{} {}".format("Christoph", "Hartleb")

def function_2():
    return f"{'Christoph'} {'Hartleb'}"

if __name__ == "__main__":
    main()