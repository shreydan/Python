# bubble sort

def bubble(sortlist):
	"""checks for adjacent values and swaps them on the spot"""
	
	for i in range(0,len(sortlist)):
		for j in range(0,len(sortlist)-1):
			if sortlist[j] > sortlist[j+1]:
				sortlist[j],sortlist[j+1] = sortlist[j+1],sortlist[j]
				
	return sortlist
