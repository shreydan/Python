"""
written in Python 3 by Shreyas Daniel - github.com/shreydan
Game: 2 operators, 2 operands, 3 levels and grades accordingly.

***********************************************
* READ THIS CAREFULLY TO UNDERSTAND THE LOGIC *
***********************************************

"""

import random

correct = 0
wrong = 0

def result(correct, wrong, level):
    print ("You got %s correct and %s wrong!"%(correct,wrong))
    if level == 1:
        if correct < 5:
            print ("Grade: C")
        elif correct >= 5 and correct <= 7:
            print ("Grade: B")
        else:
            print ("Grade: A")

    if level == 2:
        if correct <7:
            print "Grade: C")
        elif correct >= 7 and correct <= 15:
            print ("Grade: B")
        else:
            print ("Grade: A")

    if level == 3:
        if correct < 13:
            print ("Grade: C")
        elif correct >= 13 and correct <= 19 :
            print ("Grade: B")
        else:
            print ("Grade: A")

def finalizer(level,questions,correct,wrong):
    if level == 1 and questions == 10:
        result(correct,wrong,level)
    elif level == 2 and questions == 15:
        result(correct,wrong,level)
    elif level == 3 and questions == 20:
        result(correct,wrong,level)

def calculator(numbers, operator, level, questions):

    if operator == '+':
        answer = float(numbers[0] + numbers[1])
    elif operator == '-':
        answer = float(numbers[0] - numbers[1])
    elif operator == '*':
        answer = float(numbers[0] * numbers[1])

    guess = float(input("\n\n" + str(numbers[0]) + " "+operator+" " + str(numbers[1]) + "\n"))
    global correct, wrong
    if guess == answer:
        correct += 1
    else:
        wrong += 1
        print ("\nCorrect answer: %s"%answer)

    finalizer(level,questions,correct,wrong)

def levels(level,questions):
    operators = ['+','-','*']
    op = random.randint(0,2)
    operator = operators[op]

    global numbers
    numbers=[]
    if level==1:
        while len(numbers) <= 1:
            numbers.append(float(random.randint(1,15)))
    elif level==2:
        while len(numbers) <= 1:
            numbers.append(float(random.randint(5,20)))
    elif level==3:
        while len(numbers) <= 1:
            numbers.append(float(random.randint(10,30)))

    calculator(numbers,operator,level,questions)

def loop(level):
    questions = 1
    if level==1:
        while questions <= 10:
            levels(level,questions)
            questions+= 1
    elif level==2:
        while questions <= 15:
            levels(level,questions)
            questions+= 1
    elif level==3:
        while questions <= 20:
            levels(level,questions)
            questions+= 1

def difficultyselector():
    level = int(input("1. Easy\n2.Medium\n3. Hard\n\n"))
    if level==1:
        loop(level)
    elif level==2:
        loop(level)
    elif level==3:
        loop(level)

def welcome():
    print ("The Math Game\nCoded with <3 by Shreyas Daniel\n2016\n")
    difficultyselector()

welcome()
