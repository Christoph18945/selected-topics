#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Singleton Method

In this example, the StrategyInterface defines a common method (do_operation), and there are two concrete strategies (ConcreteStrategyA
and ConcreteStrategyB) that implement this interface. The Context class has a single method (execute_strategy), which delegates the
execution to the strategy.

This example follows a design pattern (Strategy Pattern) where a class appears to have a single method (execute_strategy), but the
behavior is determined by the strategy that is injected into the class. This approach provides flexibility and allows you to change
the behavior of the class by swapping the strategy at runtime.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

def main() -> None:
    """mian function"""
    strategy_a = ConcreteStrategyA()
    context_a = Context(strategy_a)
    context_a.execute_strategy()

    strategy_b = ConcreteStrategyB()
    context_b = Context(strategy_b)
    context_b.execute_strategy()

    return None
class StrategyInterface:
    """Interface class"""
    def do_operation(self):
        """"""
        pass

class ConcreteStrategyA(StrategyInterface):
    """"""
    def do_operation(self):
        """"""
        print("Strategy A is executed.")

class ConcreteStrategyB(StrategyInterface):
    """"""
    def do_operation(self):
        """"""
        print("Strategy B is executed.")

class Context:
    """"""
    def __init__(self, strategy):
        """"""
        self._strategy = strategy

    def execute_strategy(self):
        """"""
        self._strategy.do_operation()

if __name__ == "__main__":
    main()
