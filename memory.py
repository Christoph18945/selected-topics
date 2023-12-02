#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Memory:
    """class represents memory locations of variables"""
    def __init__(self) -> None:
        """initialize class"""
        return None

    def get_mem_addr(self,variable: int) -> str:
        """print hex value of integer"""
        hex_value = hex(id(variable))
        return hex_value