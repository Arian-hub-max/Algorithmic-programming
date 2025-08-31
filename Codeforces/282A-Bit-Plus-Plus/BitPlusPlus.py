def customizedInput():    
    n = int(input())
    arr = []
    binary = {0,1}
    num_of_solutions = 0
    if n < 1 or n > 150: 
        print("the number is invalid. It should be between 1 and 100.")
    for i in range(n):
        #we separate the input by space instead of lines and then map and list it. 
        line = input()
        arr.append(line)
    return arr


#We use a sequential if statement to assign the string value of incrementation or decrementation to the mathematical value
def calculateX():
    x = 0
    array = customizedInput()
    for i in range(len(array)):
        if array[i] == "X":
            x = 0
        if array[i] == "X++" or array[i] == "++X":
            x += 1
        if array[i] == "X--" or array[i] == "--X":
            x -= 1

    print(x)
calculateX()