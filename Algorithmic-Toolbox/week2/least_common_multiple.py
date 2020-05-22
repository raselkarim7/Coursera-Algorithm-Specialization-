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

def lcm_naive(a, b):

    current_gcd = gcd_naive(a, b)
    # print('xxxxxx ', current_gcd)
    current_lcm = (a*b)/current_gcd
    # print ('current lcm ========== ', a*b, current_lcm)
    return int(current_lcm)

if __name__ == '__main__':
    # input = sys.stdin.read()
    inputData = input()
    a, b = map(int, inputData.split())
    print(lcm_naive(a, b))

