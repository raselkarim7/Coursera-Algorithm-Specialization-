import random
import time

def maxPairwiseProductMultiply(num_list):
    bigNum = 0
    bigNumIdx = 0
    
    secondBigNum = 0
    
    for idx, i in enumerate(num_list): 
        if i > bigNum: 
            bigNum = i
            bigNumIdx = idx # if same biggest number exists duplicate to compare it later.
    
    for idx, i in enumerate(num_list): 
        if i > secondBigNum and idx != bigNumIdx : 
            secondBigNum = i

    return bigNum * secondBigNum

if __name__ ==   '__main__': 
    # num_list_map = map(lambda param: param * random.randint(10, 5000),  [1] * 1000000)
    # num_list = list(num_list_map)
    # print( num_list )
    # exit()
    
    num_list = []
    count = int(input())    
    num_list =  list( map(int, input().split()) )

    # for i in range(count):
    #     item = int(input())
    #     num_list.append(item)

    sum = maxPairwiseProductMultiply(num_list)
    print(sum)
