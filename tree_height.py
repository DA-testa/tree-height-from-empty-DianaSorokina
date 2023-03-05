# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    height = [0] * n
    for i in range(n):
       if height[i] == 0:
           cur_h = 1
           br = i
           while parents[br] != -1:
             br = parents[br]
             if height[br] !=0:
                 cur_h += height[br]
                 break
             cur_h += 1
           height[i] = cur_h
    return max(height)

def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements 
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
       
        n = input().strip()
        if n =='I':
            n = int(input())
            parents = list(map(int,input().split()))
            print(compute_height(n,parents))
        elif n =='F':
            file = input()
            with open("./test/"+file, 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
                print(compute_height(n,parents))
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
