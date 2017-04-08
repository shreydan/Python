"""
Written in Python 3

Description: writes "n" prime nos to a file.
teaches while loop, defining function and calling it, file input.
Written by: Shreyas Daniel github.com/shreydan

Catch: This program is VERY slow when generating a lot of prime nos.
	   It took around 6.5 seconds to generate 1000 primes
This program is all yours now!
"""

def write_to_file(primes):
	f = open("primes.txt","w+") # creates file if it doesn't exist
	for pnos in primes:
		pnos = str(pnos)+"\n"
		f.write(pnos)
	
	print ("The primes are in the file primes.txt")
	

def prime():
    
    primes = []
    i = 1
    num = 2
    n = int(input("Enter the no. of prime nos. you want\n>>> "))
    print ("generating...")
    while len(primes) < n: # loop to generate n prime nos.
        count = 0
	i = 1
        while i <= num: # loop to generate factors of a no.
            if num%i==0:
                count += 1
            i+=1

        if count == 2: # checks if it's a prime no.
            primes.append(num) 

        num += 1

    write_to_file(primes)

prime()
