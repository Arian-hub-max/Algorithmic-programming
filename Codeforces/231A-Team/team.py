def customizedInput():    
    n = int(input())
    arr = []
    binary = {0,1}
    num_of_solutions = 0
    if n < 1 or n > 1000: 
        print("the number is invalid. It should be between 1 and 100.")
    for i in range(n):
        #we separate the input by space instead of lines and then map and list it. 
        question = list(map(int,input().split()))
        if len(question) != 3 or not set(question).issubset(binary):
            print("That is wrong")
            return False
        if verify_solution(question):
            num_of_solutions += 1
    print(num_of_solutions)
        
        

def verify_solution(triple):
    if triple.count(1) >= 2:
        return True



customizedInput()