def compare(a,b):

    alice = 0
    bob = 0
    result = []
    size = len(a)

    for i in range(size):
        if a[i] > b[i]:
            alice = 1 + alice
        elif b[i] > a[i]:
            bob = 1 + bob

    result.append(alice)
    result.append(bob)

    return result


a = [1,4,10]
b = [2,4,1]

print_resolution = compare(a,b)
print(print_resolution)