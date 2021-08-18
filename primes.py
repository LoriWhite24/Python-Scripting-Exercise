# Author: Lori White
# This program prints the primes from a to b, which are specified by the user.
# a and b must be an integer and a < b.
from math import sqrt

# Checks if the number is prime or not
def isPrime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i == 0):
                return False
    return True

# Finds all the primes and saves them to a list
def findPrimes(a, b):
    primes = []
    for n in range(a, b + 1):
        if isPrime(n):
            primes.append(n)
    return primes

# Prints the list of primes
def getPrimes(primes):
    return ','.join([ n for n in primes])[:-1]

# Gets the user's specified value a
def getA():
    a = 0.1
    while str(type(a)) != "int":
        try:
            a = int(input("\nEnter the value you wish to start listing from: "))
        except ValueError:
            print("You must enter an integer! Please, try again.")
    return a

# Gets the user's specified value b
def getB(a):
    b = 0.1
    while str(type(b)) != "int":
        try:
            b = int(input("\nEnter the value you wish to end the listing at: "))
            checkValue(a, b)
        except ValueError:
            print("You must enter an integer! Please, try again.")
        except AssertionError as e:
            print(f"{e} Please, try again.")
    return b

# Checks if a < b
def checkValue(a, b):
    assert (a < b), f"The ending value cannot be equal to or less than the starting value, {a}!"

# Gets the user's choice for exiting the program 
def getOption():
    option = ""
    contain = False
    while not contain :
        try:
            option = input("\nDo you wish to exit this program? (Y/N)  ").upper()
            contain = checkOption(option)
        except AssertionError as e:
            print(f"{e} Please, try again.")
    if "Y" in option:
        return True
    else:
        return False

# You must enter Y or N!
def checkOption(option):
    assert ("Y" in option or "N" in option), "You must enter Y or N!"
    return True

# Runs the Prime Checker program
def primeChecker():
    print("Welcome to Prime Checker!\nHere you can list all the primes for a specified range of values.\n")
    exit = False
    while not exit:
        first = getA()
        last = getB(first)
        primes = getPrimes(findPrimes(first, last))
        print(f"\nThe primes within the range of {first} and {last} are {primes}.\n")
        exit = getOption()
    print("\nGoodbye!")

# Main Program
primeChecker()