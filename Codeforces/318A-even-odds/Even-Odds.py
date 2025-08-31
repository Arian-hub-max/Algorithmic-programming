"""
def even_odds():
    n, k = map(int, input().split())
    arr = []
    for odd_num in range(1,n+1,1):
        arr.append(odd_num)
    for even_num in range(2,n+1,2):
        arr.append(even_num)
    
    print(arr[k-1])

even_odds()

def even_odds():
    n, k = map(int, input().split())
    odd_arr = []
    even_arr = []
    for num in range(1,n+1,1):
        if num %2 != 0:
            odd_arr.append(num)
        else: 
            even_arr.append(num)
    arr = odd_arr + even_arr
    print(arr[k-1])

even_odds()

"""

def even_odds():
    n, k = map(int, input().split())

    #the first subset which is the odd numbers
    odd_count = (n + 1) // 2
    
    if k <= odd_count:
        print(2 * k - 1)   # k-th odd
    else:
        print(2 * (k - odd_count))  # (k - odd_count)-th even

even_odds()