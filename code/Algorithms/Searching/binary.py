# binary search

def binary(srchlist,srch):
	"""list needs to be in ascending order to search for element"""
	
	first = 0
	last = len(srchlist)-1
	while first <= last:
		mid = (first + last)/2
		if srch > srchlist[mid]:
			first = mid+1
		elif srch < srchlist[mid]:
			last = mid-1
		else:
			return mid
	
	return -1

