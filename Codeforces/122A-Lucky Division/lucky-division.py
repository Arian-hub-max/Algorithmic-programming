"""
I solved the problem by using two functions. 

The first function lucky_number() gets an input and check if it only contains the letters 4 and 7.
In the second function verifier(), I iterate through all the numbers smaller than the actual input and check if the divisor is lucky number
and the the number is divisable (i.e. the modulus function is zero)
"""

def is_lucky_number(num):
    num = str(num)
    for digit in num:
        if digit != "4" and digit != "7": #if used or, an input like 24 would be correct
            return False
    return True
    



def verifier():
    num = int(input())
    for divisor in range(1,num+1):
        if is_lucky_number(divisor) and num %  divisor == 0:
            print("YES")
            break
    else:
        print("NO")

verifier()