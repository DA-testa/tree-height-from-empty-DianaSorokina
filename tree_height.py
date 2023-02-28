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
                if height [br] != 0:
                    cur_h += height[br]
                    break
                cur_h += 1
            height[i] = cur_h
    return max(height)


def main():
    # implement input form keyboard and from files
    input_source = input()
    if input_source == 'file':
        filename = input()
        if 'a' in filename:
            print(invalid file)
            break;
         with open(filename, 'r') as f:
            n= int(f.readline().strip())
            parents = list(map(int, f.readline().strip.split()))
    else:
        n = int(input())
        parents = list(map(int, input().split()))
        
    print(compute_height(n. parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    #n = int(input())
    # input values in one variable, separate with space, split these values in an array
    #parents = list(map(int, input().split()))
    # call the function and output it's result
    #print(compute_height(n. parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
