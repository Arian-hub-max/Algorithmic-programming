"""
The ideal solution for both parties is to have the equal share. However since one of the twins is greedy but needs the
the other twin to have at least one coin. We would sort the coins in a descending order (so we can get the maximal
value by adding the highest amount first) and then continue till our share is stricly higher than the other's twin's share
In other words:
our share > total value - ourshare
"""

def choose_coins():
    n= int(input())
    coins = list(map(int,input().split()))
    coins = sorted(coins, reverse=True)
    total_sum = sum(coins)
    greedy_sum = 0
    count = 0
    if len(coins) != n:
        print("The number of coins should be " + n)
    else:
        for coin in coins:
            greedy_sum += coin
            count += 1
            if greedy_sum > total_sum - greedy_sum:
                break
    
    print(count)

choose_coins()

