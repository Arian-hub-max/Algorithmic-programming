"""
In this approach, we define the x, y, and z axes as arrays, after getting the vector inputs (as lists) and do initial checking of the
existance of all coordinates, we append each corresponding element of each vector to the corresponding array. 

according to the mathematical standard, we know that: 

first element: x-axis
second element: y-axis
third element: z-axis

after the loop, we check if the sum of all three arrays is zero (i.e. the net force is zero) and prints the final answer accordingly
"""

def is_equilibirium():

    number_of_vectors = int(input())

    x_axis = []
    y_axis = []
    z_axis = []

    for i in range(number_of_vectors):

        vector = list(map(int,input().split()))

        if len(vector) != 3:

            print("All 3 coordinates are required!")
            return False
        
        x_axis.append(vector[0])
        y_axis.append(vector[1])
        z_axis.append(vector[2])

    if sum(x_axis) == 0 and sum(x_axis) == 0 and sum(x_axis) == 0:
        
        print("YES")

    else:

        print("NO")



is_equilibirium()