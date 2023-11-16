#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""calbback example"""

def main() -> None:
    """main function"""
    num = (8, 5)
    ans = Callbacks().caller(Callbacks().called, num)
    print("Multiplication =", ans)
    return None

class Callbacks:
    """Callbacks class"""

    def __init__(self):
        """"""

    def called(self,n: int) -> int:
        """called function"""
        return n[0]*n[1]

    def caller(self, func: object, n: object):
        """caller function"""
        return func(n)

if __name__ == "__main__":
    main()
