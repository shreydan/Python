"""
Written in Python 3
Description: converts string to binary
Written by: Shreyas Daniel github.com/shreydan
"""

def tobin(string):
	bstring = "" # new empty string
	for char in string:
		ochar = bin(ord(char)).replace("0b","0") # string[char] -> ord -> bin -> replace
		bstring += (str(ochar) + " ") # add space
	
	return bstring.strip(' ') #remove trailing white space
	
string = input("Text to Binary\n>>> ")
print (tobin(string))
