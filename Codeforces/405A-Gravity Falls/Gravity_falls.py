"""
If we use our imagination and look at the sample outputs, we can see a pattern; The columns of toy cubes get sorted in an ascending order
e.g. if we have the following: 5 4 2 3
after tilting it 90 degrees clockwise, we would have: 2 3 4 5
If we have: 10 8 5 2 4
then after the fall, we would have: 2 4 5 8 10

So we simply need to sort the columns in an ascending order
"""

def Gravity_Falls():
    n = int(input())

    cubes = list(map(int, input().split()))
    if len(cubes) != n:    
        print("That is the wrong number of columns")
    else:
        print(*sorted(cubes)) #using * will unpack the array and convert it to a space-separated string

Gravity_Falls()
