def anagramsolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramsolution2('abcd','acbd'))

"""
- At first glance you may be tempted to think that this algorithm is O(n),
- However, the two calls to the Python sort method are not without their own cost. As we will see in a later chapter, sorting is typically either O(n2) or O(nlogn), so the sorting operations dominate the iteration. In the end, this algorithm will have the same order of magnitude as that of the sorting process.

"""