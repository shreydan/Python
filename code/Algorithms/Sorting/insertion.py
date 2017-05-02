# insertion sort

def insertion(sortlist):
    """starts from index 1, sorts everything behind and moves forward."""

    for i in range(1,len(sortlist)):
        element = sortlist[i]
        j = i
        while j > 0 and sortlist[j-1] > element:
            sortlist[j] = sortlist[j-1]
            j = j - 1
        sortlist[j] = element
    
    return sortlist
                
