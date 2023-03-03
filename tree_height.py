# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    height = [-1] * n
    for i in range(n):
        if heights[i] != -1:
            continue
        height =1
        cur_h = i
        while parents[cur_h] != -1:
           if heights = parents[cur_h]
               height += heights[cur_h]
               break
           else:
                cur_h = parents[cur_h]
                height += 1
        heights[i] = height  
    return max(heights)


def main():
    # implement input form keyboard and from files
    #
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    try:
        file_name = input().strip()
        while 'a' in file_name:
            file_name = input().strip()
    except EOFError:
        return
    
    # input number of elements
    try:
        n = int(input().strip())
    # input values in one variable, separate with space, split these values in an array
        parents = list(map(int, input().split()))
    # call the function and output it's result
        print(compute_height(n, parents))
    except (EOFError, ValueError):
        return
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
