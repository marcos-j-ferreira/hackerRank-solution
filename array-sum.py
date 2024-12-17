def simpleArraySum(ar):
    sum = 0
    for x in ar:
        sum = sum + x
        
    return sum


ar = [1,2,3,4]

sum = simpleArraySum(ar)

print(sum)