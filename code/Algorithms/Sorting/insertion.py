# insertion sort

def insertion(sortlist):
    """starts from index 1, sorts everything behind and moves forward."""

    for index in range(1,len(sortlist)):
        value = sortlist[index]
        i = index-1
        while i>=0:
            if value < sortlist[i]:
                sortlist[i+1] = sortlist[i]
                sortlist[i] = value
                i-=1
            else:
                break
                
    return sortlist
                
