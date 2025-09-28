"""
We would not include + in the if condition because it does not produce any output. It just increases the correspoding
value by 1
"""
def check_for_joke():
    word = input()
    if ("H" in word) or ("Q" in word) or ("9" in word):
        print("YES")
    else:
        print("NO")

check_for_joke()