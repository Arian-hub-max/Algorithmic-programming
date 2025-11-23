"""
We follow the following pseudo-algorithm in this function:

1. the string input is defined
2. We define an array consisting of vowels (both lowercase and uppercase)
3. We define an empty string
4. We iterate through each character in the input string and compares it against the elements within the array. If same, we add it to the empty string
5. At the end, we use join function to put dot between each letter in the new string (the first "." is for the begining of the result)
"""

def transform_string():
    word = str(input())

    vowels = ["A", "O", "Y", "E", "U", "I","a","o","y","e","u","i"]
    word_with_no_vowels = ""
    for char in word:
        if char in vowels: #do we need if statement?
            continue
        word_with_no_vowels += char
        
    
    #add . before each character

    result = "." + ".".join(word_with_no_vowels.lower()) #convert all letters to lower-case
    print(result)

transform_string()


