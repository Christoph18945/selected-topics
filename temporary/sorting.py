#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""sorting algorithms
"""

def insertion_sort(list_to_sort: list) -> None:
    """Insertion sort algorithm"""
    print(f"Unsorted : {list_to_sort}")
    # iterate over array to be sorted
    for i in range(1, len(list_to_sort)):
        x = list_to_sort[i] # get each element
        j = i-1 # get one position before x
        # shift until reaching index 0 or getting an element smaller than x
        while j>=0 and x<list_to_sort[j]:
            # swap here
            list_to_sort[j+1] = list_to_sort[j]
            j = j-1
        # keep as it is
        list_to_sort[j+1] = x
    print(f"Sorted : {list_to_sort}")

def merge_sort(input_list: list):
    """Merge sort"""
    # check if list exists
    if len(input_list) > 1:
        # finding mid of list, ...
        mid = len(input_list)//2
        # dividing the list elems ...
        left_part = input_list[:mid]
        # into 2 halves
        right_part = input_list[mid:]
 
        # sorting both halfs
        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0

        # copy data to temp lists
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                input_list[k] = left_part[i]
                i += 1
            else:
                input_list[k] = right_part[j]
                j += 1
            k += 1

        # check if element was left
        while i < len(left_part):
            input_list[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            input_list[k] = right_part[j]
            j += 1
            k += 1

def quick_sort(unsorted_list: list):
    """Quick sort"""
    elements = len(unsorted_list)
    # base case
    if elements < 2:
        return unsorted_list
    current_position = 0 #Position of the partitioning element
    for i in range(1, elements): #Partitioning loop
         if unsorted_list[i] <= unsorted_list[0]:
              current_position += 1
              temp = unsorted_list[i]
              unsorted_list[i] = unsorted_list[current_position]
              unsorted_list[current_position] = temp

    temp = unsorted_list[0]
    unsorted_list[0] = unsorted_list[current_position] 
    unsorted_list[current_position] = temp #Brings pivot to it's appropriate position
    left = quick_sort(unsorted_list[0:current_position]) #Sorts the elements to the left of pivot
    right = quick_sort(unsorted_list[current_position+1:elements]) #sorts the elements to the right of pivot
    unsorted_list = left + [unsorted_list[current_position]] + right #Merging everything together 

    return unsorted_list

def heap_sort(arr):
    """Heap sort
    """
    n = len(arr)
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        # Change root, if needed
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
    
        # Heapify the root.
        heapify(arr, n, largest)
  
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements
  
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
              
def bucket_sort(x):
    """Bucket sort
    """
    def insertionSort(b):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while j >= 0 and b[j] > up: 
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up     
        return b 

    arr = []
    slot_num = 10 # 10 means 10 slots, each
                  # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])
          
    # Put array elements in different buckets 
    for j in x:
        index_b = int(slot_num * j) 
        arr[index_b].append(j)
      
    # Sort individual buckets 
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
          
    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x

def counting_sort(arr):
    """Counting sort
    """
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
 
    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]
 
    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]
 
    # Store count of each character
    for i in arr:
        count[ord(i)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]
 
    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

# // A utility function to get maximum value in arr[]
# int getMax(int arr[], int n)
# {
#     int mx = arr[0];
#     for (int i = 1; i < n; i++)
#         if (arr[i] > mx)
#             mx = arr[i];
#     return mx;
# }

# // The main function to that sorts arr[] of size n using
# // Radix Sort
# void radixsort(int arr[], int n)
# {
#     // Find the maximum number to know number of digits
#     int m = getMax(arr, n);
  
#     // Do counting sort for every digit. Note that instead
#     // of passing digit number, exp is passed. exp is 10^i
#     // where i is current digit number
#     for (int exp = 1; m / exp > 0; exp *= 10)
#         countSort(arr, n, exp);
# }

    # modules/sorting.py
    # insertion_sort([1,3,2.4,8,1,9,0])
    # insertion_sort(["c", "a", "d"])
    # merge_sort([1,3,2.4,8,1,9,0])
    # quick_sort([1,3,2.4,8,1,9,0])
    # heap_sort([1,3,2.4,8,1,9,0])
    # bucket_sort([1,3,2.4,8,1,9,0])
    # counting_sort([1,3,2.4,8,1,9,0])