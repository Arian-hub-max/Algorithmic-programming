"""
The problem with the below algorithm is that the index() function will fail if the character does not exist
"""
"""
def is_hello():

    word = str(input())
    hello = "hello"
    
    for char in hello:
        if word.count(char) < hello.count(char):
            print("NO")
            raise SystemExit #stops the whole function

    H = word.index("h".lower())
    E = word.index("e".lower(),H+1)
    L = word.index("l".lower(),E+1)
    L_2 = word.index("l".lower(), L+1)  #we can not use word[L+1:].index("l".lower()) because it would start the index from 0
    O = word.index("o".lower(),L_2+1)


    if H < E < L < L_2 < O:
        print("YES")
    else:
        print("NO")
    

is_hello()
"""

"""

In this approach, We use try-catch approach. in the try clause, we find the index number of each designated character ('h','e','l','l','o')
sequentially (by looking for the next character right after the previous one)

In the catch clause (any other scenario e.g. If one/more character does not exists), we throw an error and print "NO"
we throw 
"""
def is_hello():

    word = input()

    # Remove your incorrect existence check!
    # Because .index() will fail naturally if order is impossible.

    try:
        H = word.index("h")
        E = word.index("e", H+1)
        L = word.index("l", E+1)
        L_2 = word.index("l", L+1)
        O = word.index("o", L_2+1)
        print("YES")
    except ValueError:
        print("NO")

is_hello()