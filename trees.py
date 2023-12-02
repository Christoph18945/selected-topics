#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Examples for tree traversals
"""

from typing import Any


def main() -> None:
    """main function"""
    # modules/trees.py
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\nInorder traversal of binary tree is")
    print_in_order(root)

    # Lowest common ancestor
    # -----------------------
    # Let's create the Binary Tree shown in above diagram
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
     
    print("LCA(4, 5) = %d" % (findLCA(root, 4, 5,)))
    print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
    print("LCA(3, 4) = %d" % (findLCA(root, 3, 4)))
    print("LCA(2, 4) = %d" % (findLCA(root, 2, 4))) 

    # find k-smallest element in BST (order statics in BST)
    # root = None
    keys = [20, 8, 22, 4, 12, 10, 14]
 
    for x in keys:
        root = insert(root, x)
 
    k = 3
 
    print_kth_smallest(root)

    return None

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_in_order(root):
    """A function to do inorder tree traversal.
    """
    if root:
        # First recur on left child
        print_in_order(root.left)
        # then print the data of node
        # print(root.val),
        # now recur on right child
        print_in_order(root.right)
 
# Python Program for Lowest Common Ancestor in a Binary Tree
# -----------------------------------------------------------
# O(n) solution to find LCS of two given values n1 and n2

# class Node:
#    """A binary tree node."""
#    # Constructor to create a new binary node
#    def __init__(self, key):
#        self.key = key
#        self.left = None
#        self.right = None
 
# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath(root, path, k):
    # Baes Case
    if root is None:
        return False
 
    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    # path.append(root.key)
 
    # See if the k is same as root's key
    # if root.key == k:
    #    return True
 
    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True
 
    # If not present in subtree rooted with root, remove
    # root from path and return False
 
    # path.pop()
    return False
 
# Returns LCA if node n1 , n2 are present in the given
# binary tree otherwise return -1
def findLCA(root, n1, n2):
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []
 
    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
 
    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

# Recursive function to insert an key into BST
 
# A simple inorder traversal based Python3
# program to find k-th smallest element
# in a BST.
# A BST node
#class Node:
#    def __init__(self, key):
#        self.data = key
#        self.left = None
#        self.right = None
 
# Recursive function to insert an key into BST
def insert(root, x):
    if (root == None):
        return Node(x)
    if (x < root.data):
        root.left = insert(root.left, x)
    elif (x > root.data):
        root.right = insert(root.right, x)
    return root
 
# Function to find k'th largest element
# in BST. Here count denotes the number
# of nodes processed so far
 
def kthSmallest(root):
    global k
    # Base case
    if (root == None):
        return None
 
    # Search in left subtree
    left = kthSmallest(root.left)
 
    # If k'th smallest is found in
    # left subtree, return it
    if (left != None):
        return left
 
    # If current element is k'th
    # smallest, return it
    # k -= 1
    # if (k == 0):
    #     return root
 
    # Else search in right subtree
    # return kthSmallest(root.right)
 
def print_kth_smallest(root):
    """Function to find k'th largest element in BST
    """
 
    res = kthSmallest(root)
 
    if (res == None):
        print("There are less than k nodes in the BST")
    else:
        print("K-th Smallest Element is ", res.data)

if __name__ == "__main__":
    main()
