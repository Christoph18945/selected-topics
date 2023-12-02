#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import unittest

class TestDemo:
    """
    white-box tests
    The test3( ) method is commented out because, as you’ll see, it causes
    the automatic build of this book’s source-code tree to stop. Add Comment
    You can name your inner class anything you’d like; the only important
    factor is that it extends UnitTest. You can also include any necessary
    support code in other methods. Only public methods that take no
    arguments and return void will be treated as tests (the names of these
    methods are also not constrained). Add Comment
    The above test class creates two instances of TestDemo. The TestDemo
    constructor prints something, so that we can see it being called. You could
    also define a default constructor (the only kind that is used by the test
    framework), although none is necessary here. The TestDemo class has a 
    close( ) method which suggests it is used as part of object cleanup, so this
    is called in the overridden cleanup( ) method in Test. Add Comment
    The testing methods use the affirm( ) method to validate expressions,
    and if there is a failure the information is stored and printed after all the
    tests are run. Of course, the affirm( ) arguments are usually more
    complicated than this; you’ll see more examples throughout the rest of
    this book. Add Comment
    Notice that in testB( ), the private field objCounter is accessible to the
    testing code—this is because Test has the permissions of an inner class.
    Add Comment
    You can see that writing test code requires very little extra effort, and no
    knowledge other than that used for writing ordinary classes. Add
    Comment
    To run the tests, you use RunUnitTests.py (which will be introduced
    shortly). The command for the above code looks like this: Add Comment
    java com.bruceeckel.test.RunUnitTests TestDemo
    """
    def __init__(self, s: str):
        self.obj_counter: int = 0
        self.id: int = self.obj_counter+1
        print (s + ": count = " + str(id))

    def close(self):
        print ("Cleaning up: " + id)

    def some_condition(self) -> None:
        return None
    
    def objCounter(self):
        for i in range(random.randint(0,10)):
            print(i)

class Test(unittest.main):
    def __init__(self):
        self.test_1 = TestDemo("test1")
        self.test_2 = TestDemo("test2")

    def cleanup(self):
        self.test_2.close()
        self.test_1.close()

    def test_a(self):
        print("TestDemo.testA")
        # self.assertIsNotNone(self.test_1.some_condition())

    def test_b(self):
        print("TestDemo.testB")
        # self.assertIsNotNone(self.test_2.some_condition())
        # self.assertIsNotNone(TestDemo.objCounter != 0)
        # Causes the build to halt:
        def test_3(self):
            self.assertTrue(0) 