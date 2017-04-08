# selection sort

def selection(sortlist):
	""" checks for the largest and then replaces - ascending order only"""
	
	for i in range(0,len(sortlist)-1):
		small = sortlist[i]
		pos = i
		for j in range(i+1,len(sortlist)):
			if sortlist[j] < small:
				small = sortlist[j]
				pos = j
		
		sortlist[pos] = sortlist[i]
		sortlist[i] = small;
		
	return sortlist
		
