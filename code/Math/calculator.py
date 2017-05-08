"""
Written by: Shreyas Daniel - github.com/shreydan
Description: Uses Pythons infamous eval() function as a way to implement calculator
"""

def calc(k):

    for i in k.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz!@#$%&\{}[]:;<>?':
            print ("INVALID")
            exit()
    
    try:
        k = eval(k)
    except ZeroDivisionError:
        print ("Can't divide by 0")
        exit()
    
    return k


print ("\nAvoid alphabets, symbols, = and ? characters in the input.\n")

k = input("What is ")

k = k.replace('^','**')
k = k.replace('=','')
k = k.replace('?','')

print ("\n" + str(calc(k)))
