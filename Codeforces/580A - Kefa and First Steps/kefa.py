"""
To solve this problem, I have used the bubble-sort approach; meaning that I compare every 2 numbers. The pseudoalgorithm is:

1. We intialize the inputs of the number of numbers and numbers themselves
2. We initialize the subset length as 1 (the minimum sample size if the whole numbers are in descending order)
3. we intialize an array
4. We initilize the index as 1 (because we want to compare the element in the greater index to the element in the smaller index)
5. We use a while loop: While we have not reached outside the loop (one index after the last element)
    a. if the rhs element is smaller than lhs element, then we record/append the current streak/sample size and reset it to 1
        (so we can count again for the next subset) and go to the next index
    b. else, if the order is ascending (rhs element is larger or equal to lhs element), we increment the streak by 1 and go to the next 
        element and finally append the final streak value to the records array.
6. At the end, our array will have a minimum of 1 streaks. We print out the maximum value (largest ascending order subset) of the records.
    
"""

def kefa():
    n = int(input())
    numbers = list(map(int, input().split()))
    streak = 1
    records = []
    i = 1
    while i < n:
        if numbers[i] < numbers[i-1]:
            records.append(streak)
            streak = 1
            i+=1
            continue
        i += 1
        streak += 1
    records.append(streak)
    
    print(max(records))

kefa()