"""
In order to it kxk squares in the mxm square, we can have the following approach:
if a a total area of the theater square is divisable by the flagstones, then the number would be directly
their division answer. Otherwise, there would be an additional square for each dimensione i.e. width and length.
"""

import math

def theater_square():
    n, m, a = map(int, input().split())
    print(math.ceil(n/a) * math.ceil(m/a))

theater_square()


"""
The following algorithm is a similar approach but has more steps and higher complexity.
"""
"""

def theater_square():
    n,m, k = map(int, input().split())

    whole_number = (m*n) // (k*k)
    remainder_of_whole_number = (m*n) % (k*k)
    if (remainder_of_whole_number == 0):
        print(whole_number)
    else:
        max_number_of_complete_squares = (m//k)*(n//k)
        width_incompleted_square = m//k
        length_incompleted_square = n//k
        extra_square_for_the_remainder = 1
        print(max_number_of_complete_squares + (width_incompleted_square)+(length_incompleted_square)+extra_square_for_the_remainder)

theater_square()

"""