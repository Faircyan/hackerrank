
def rotLeft():

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    return d, a

result = ""
time, list = rotLeft()

for i in range(time, len(list)+time):
    i = i % len(list)
    result += str(list[i]) + " "

print(result)
