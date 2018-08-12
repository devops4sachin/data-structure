def bubbleSortOpt(alist):
    numpass = len(alist)-1
    swapped = True
    while numpass > 0 and swapped:
        swapped = False
        for i in range(numpass):
            if alist[i] > alist[i+1]:
                swapped = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        numpass = numpass-1
    print("exiting the sorting now at iteration {}".format(numpass))


alist=[20,30,40,90,50,60,70,80,100,110]
bubbleSortOpt(alist)
print(alist)

