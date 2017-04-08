"""
Written in Python 3.
 
This program is all yours now! Have fun experimenting!!

Collatz conjecture: Count steps to reach 1 from n. If even: divide n by 2
if odd: multiply n by 3 and add 1.

teaches: creating functions, function calling, loops, loops with else (Python's cool!).
"""

def collatz(n): # collatz function with n as parameter.
	step = 0
	num = n
	while(True):
		if n % 2 == 0:
			n = n/2
			step += 1
		elif n % 2 != 0 and n != 1:
			n = n *3 + 1
			step += 1
		elif n == 1:
			step += 1
			break
	
	print ("It took %s steps to reach 1 with %s"%(step,num))
			
def input():
	# takes input and rejects it to use it as an argument till it's neither 1 nor 0.
	n= int(input("Enter a no. "))
	while n==1 or n == 0:
		print ("Nope, Another..")
		input()
	else:
		collatz(n) # call collatz function with n as argument
		
input() #calls input function

# written by @shreydan. github.com/shreydan
