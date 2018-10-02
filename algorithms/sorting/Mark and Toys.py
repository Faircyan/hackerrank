def mergeSort (alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def maximumToys():

    budget = input().split()[1]
    prices = list(map(int, input().rstrip().split()))
    return budget, prices


budget, list = maximumToys()

mergeSort(list)
budget = int(budget)
counter = 0

for i in list:
    if(budget >= i):
        budget -= i
        counter += 1
print(counter)
