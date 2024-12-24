def aVeryBigSum(arr):
    sum = 0

    for i in arr:
        sum = i + sum 

    return sum


arr = [1000000001,1000000002,1000000003, 1000000004, 1000000005]
resultion = aVeryBigSum(arr)

print(resultion)