# Efficient Fibonacci

# Uses python3
f = [None] * 10000
# print(f)
def calc_fib(n):
    if (n <= 1):
        return n

    if (f[n] != None):
        return  f[n]

    f[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return  f[n]

n = int(input())
print(calc_fib(n))
