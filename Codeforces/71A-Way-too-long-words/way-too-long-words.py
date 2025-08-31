def customizedInput():    
    n = int(input())
    arr = []
    if n < 1 or n > 100: 
        print("the number is invalid. It should be between 1 and 100.")
    for i in range(n):
        line = input()
        arr.append(line)
    filtered_arr = [myWord for myWord in arr if not any(letter.isupper() for letter in myWord)]

    for singleWord in filtered_arr:
        wordLength(singleWord)

def wordLength(word):
    if len(word) > 10:
        print(word[0] + str(len(word[1:-1])) + word[-1])
    else:
        print(word)



customizedInput()
"""
word = "Supermodelamooarian"
print(word[1:-1])
"""
"""
def customizedInput():    
    n = int(input("Enter number of words: "))
    for i in range(n):
        line = input("Enter word: ")
        wordLength(line)

def wordLength(word):
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print("not palindrome")  # This message is misleading — maybe change to "word is short"?

# Run the input function
customizedInput()
"""