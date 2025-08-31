#link to the problem 158A: https://codeforces.com/problemset/problem/158/A

#sys library is later used to terminate the program under certain conditions: similar to throwing exception error
import sys
def NextRound():
    
    #make the splitted input strictly integer

    n, k = map(int, input().split())
    points = list(map(int,input().split()))
    number = 0

    if len(points) != n:
        print("The number of points enetered is incorrect")
        sys.exit()

    #this checks if the points are in descending order by comparing the original array to its reversely sorted version.
    #alt way --> using a boolean value such that is_desc = all(points[i] > points[i+1] for i in range(len(points)-1))
    
    if points != sorted(points, reverse=True):
        print("The points should be ranked from top to bottom")
        sys.exit()
    for i in range(n):
        if (points[i] >= points[k-1]) and (points[i] > 0):
            number += 1
    print(number)


NextRound()

