
"""
only an even number can be the sum of 2 even numbers. On the other hand, we know that this number should be 
bigger than 2 and less than 100
"""

def watermelon_weight(weight):
    if weight % 2 == 0 and 2 < weight <= 100:
        return 'YES'
    else:
        return 'NO'

# Read input
w = int(input())

# Call the function and print the result
print(watermelon_weight(w))