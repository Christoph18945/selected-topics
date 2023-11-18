#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Memory:
    """class represents memory locations of variables"""
    def __init__(self) -> None:
        """initialize class"""
        pass

    def get_mem_addr(self,variable: int) -> hex:
        """print hex value of integer"""
        hex_value = hex(id(variable))
        return hex_value