def anagramsolution1(s1, s2):
	alist = list(s2)

	pos1 = 0
	stillOK = True
	
	while pos1 < len(s2) and stillOK:
		pos2 = 0
		found = False
		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				alist[pos2] = None
				found = True
			else:
				pos2 = pos2 + 1

		if not found:
			stillOK = False

		pos1 = pos1 + 1

	return stillOK

print(anagramsolution1('abcd','dcba'))
print(anagramsolution1('abc','def'))


""" 
- To analyze this algorithm, we need to note that each of the n characters in s1 will cause an iteration through up to n characters in the list from s2. Each of the n positions in the list will be visited once to match a character from s1.
- The number of visits(comparisions) then becomes the sum of the integers from 1 to n. We stated earlier that this can be written as,
	n(n+1) / 2.

- As n gets large, the n2 term will dominate the n term.
-  Therefore, this solution is O(n2).

"""
