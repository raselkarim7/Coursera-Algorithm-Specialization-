# Uses python3
import sys

def gcd_naive(a, b):
    if (b > a):
        a, b = b, a

    if (b == 0 or a == 0):
        return 1

    while (a % b !=0 ):
       c = a%b
       a,b = b, c

    current_gcd = b
    return current_gcd

if __name__ == "__main__":
    # input = sys.stdin.read()
    inputData = input()
    # print('input data === ', inputData)
    a, b = map(int, inputData.split())
    print(gcd_naive(a, b))


# Sample Input
# 22448866 66224488
#
# Sample Output
# 2222
