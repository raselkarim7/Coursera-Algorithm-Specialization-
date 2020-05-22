# Uses python3
# NOT_SOLVED

def getPisanoPeriod(n, divider):
    pisano = list()

    previous = 0
    current = 1
    pisano.append(previous)
    pisano.append(current)

    if n <= 1:
        return pisano

    for i in range(n):
        previous, current = current, (previous + current)
        pisano.append(current % divider)
        # There must be a repetition of "011" pisano period, so we compared
        if i > divider and "".join(map(str, pisano[-3:])) == "011":
            pisano = pisano[:(len(pisano) - 3)]
            # print(pisano)
            # print(len(pisano))
            break

    return pisano


def get_fibonacci_huge_naive(n, divider):
    pisano_period = getPisanoPeriod(n, divider)  # Returns a list
    position = n % len(pisano_period)  # As we consider 0 -> 0th, 1 -> 1st, 1 -> 2nd .... 55->10th fibonacci.
    return pisano_period[position]

if __name__ == '__main__':
    # input = sys.stdin.read();
    inputData = input()
    n, m = map(int, inputData.split())
    print(get_fibonacci_huge_naive(n, m))
