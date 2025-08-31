#we use regex library to define the schema of a binary value in a string
import re

def football_position():
    position = str(input())
    #the binary string should only have digits 0 and 1
    binary_pattern = r'^[01]+$' 

    #this condition checks if the length is more than 100 characters or digits other than 0 and 1 are being entered.
    if (not re.match(binary_pattern, position)) or (len(position) > 100):
        print("Wrong format. Only numbers 1 and 0 are allowed and the number of digits should not exceed 100")
    else:
        if ("1111111" in position) or ("0000000" in position):
            print("YES")
        else:
            print("NO")

football_position()
    