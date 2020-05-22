# Uses python3
import sys
import math

def getRangeSum(startIndex):
    repeatedPattern = '011235831459437077415617853819099875279651673033695493257291'
    res = map(int, repeatedPattern[startIndex: ])
    sum = 0
    for i in  res:
        sum = sum + i * i # The only difference from 2.7 is here.
    return sum

def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next = 1

    if to < 10 ** 1:  # This if block is not needed. Though I keep it just to see the difference between the else block
        for i in range(to + 1):
            if i >= from_:
                sum += (current % 10) ** 2

            current, next = next % 10, (current + next) % 10
    else:
        fromQuotent = math.floor(from_ / 60)
        fromReminder = from_ % 60
        toQuotent = math.floor(to / 60)
        toReminder = to % 60
        sum = getRangeSum(fromReminder) + (toQuotent - (fromQuotent + 1)) * getRangeSum(0) + getRangeSum(0) - getRangeSum(toReminder+1)
    return sum % 10


if __name__ == '__main__':
    # input = sys.stdin.read();
    inputData = input()
    to = int(inputData)
    print(fibonacci_partial_sum_naive(0, to))


# Sample Input
# 100000000

# Sample Output
# 5



