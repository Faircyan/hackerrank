def makeAnagram():

    a = input()

    b = input()

    return a, b

a, b = makeAnagram()

a = sorted(a)
b = sorted(b)

counter = 0
i = 0

while(i < len(a)):

    if(a[i] == b[i]):
        i += 1
    else:
        counter += 1
        if(a[i] < b[i]):
            a.remove(a[i])
        else:
            b.remove(b[i])

    if(i == len(a)):
        counter += len(b)-(i)
        break
    if (i == len(b)):
        counter += len(a) - (i)
        break
print(counter)