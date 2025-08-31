"""
In order to fit the 2*1 domino pieces in a m x n rectangle, We simply need to use / function in python
(getting the integer part of the result of the division) to get the max number of dominos in the rectangle/square.
"""
def max_number_of_dominos():
    m, n = map(int, input().split())
    print((m*n)//2)

max_number_of_dominos()
