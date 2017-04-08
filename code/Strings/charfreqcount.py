"""
Written in Python 3.
 
This program is all yours now! Have fun experimenting!!

This program accepts a sentence and prints the frequency of all the letters in the sentence.

teaches: creating functions, function calling, loops, bubble sort algorithm, lists (arrays), dictionary.
"""

def main():
	sentence = input("\n\nEnter a sentence\n")
	sentence = sentence.lower()
	string = sentence.replace(" ","")
	chars = []
	for char in string:
		chars.append(char)
	alphad = {}
	for i in range(0,len(chars)):
		for j in range(0,len(chars)-1):
			if ord(chars[j]) > ord(chars[j+1]):
				chars[j+1] , chars[j]=chars[j],chars[j+1]


	for i in range(0,len(chars)-1):
		abet = chars[i]
		count = 0
		for j in chars:
			if j == abet:
				count += 1
		alphad.update({abet:count})
				
	print ("\n<!---FREQUENCY---!>\n")
	for ch in alphad:
		print (ch + " : "+str(alphad[ch]))
	print ("\n\n")
	
		
main()

# written by @shreydan. github.com/shreydan
