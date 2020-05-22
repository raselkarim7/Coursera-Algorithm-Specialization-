# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        # print(current)
        previous, current = current % 10, (previous + current) % 10 # This is the trick.

    strCurrent = str(current)
    strCurrent = strCurrent[len(strCurrent) - 1 :  ]
    # print('current === ', current, strCurrent )
    return int(strCurrent)

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    # print ('n === ', n)
    print(get_fibonacci_last_digit_naive(n))
