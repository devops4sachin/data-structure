def bubbleSort(alist):
    for numpass in range(len(alist)-1,0,-1):
        for i in range(numpass):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
