# Binary Search
import time
from array import *

#binary search list
def list_search(listt, item):
    low = 0
    high = len(listt) - 1
    while low <= high:
        mid = low + high
        guess = listt[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

start_time = time.time()
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list_search(list1, 3))
list2 = [1,2,3,4,5,6,7,8,9,10.7,11.4,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
print(list_search(list2, 23))
print("List search \n--- %s seconds ---" % (time.time() - start_time))

#binary search array
def array_search(listt, item):
    low = 0
    high = len(listt) - 1
    while low <= high:
        mid = low + high
        guess = listt[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

start_time = time.time()
array1 = array('d', [1,2,3,4,5,6,7,8,9,10])
print(array_search(array1, 3))
array2 = array('d', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33])
print(array_search(array2, 23))
print("Array search \n --- %s seconds ---"% (time.time()-start_time))

# linked list

