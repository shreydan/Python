# linear search

def linear(srchlist, srch):
	"""check every element, kinda slow"""
	
	for element in srchlist:
		if element == srch:
			return srchlist.index(element)
		
	return -1
	

			
