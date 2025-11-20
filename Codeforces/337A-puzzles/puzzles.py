
"""
Pseudo algorithm:

1. As requested, we initialize the input variables for the number of students, number of puzzles, and number of pieces in each puzzle
2. We initialze an empty array, for the purpose of recording all the differences among the pieces
3. We sort the pieces (in an ascending order)
4. Inspired from bubble sort, we iterate through the sorted puzzles and go till we reach the first element of the last subset with the
number of elements being equal to the number of students. (e.g. if the number of students is 3 and number of puzzles is 6, we iterate
through the puzzles till we reach the index 4)
5. Afterwards, in each iteration, we substract the the minimum value (at index i) from the largest value within the subset.
6. We append the result to the array.
7. After the for loop, we print out the minimum difference in the array.
"""
def find_minimum():
    size_of_class,num_of_puzzles = map(int,input().split())
    puzzles = list(map(int,input().split()))
    record = []
    if len(puzzles) != num_of_puzzles:
        return False
    
    sorted_puzzles = sorted(puzzles)

    for i in range(len(sorted_puzzles)-size_of_class+1):
        difference = sorted_puzzles[i+size_of_class-1] - sorted_puzzles[i]
        record.append(difference)
    
    print(min(record))

find_minimum()

