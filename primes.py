"""
 Author: Lori White
 This program prints the primes from first to last, which are specified by the user.
 first and last must be an integer and first < last.
"""
from math import sqrt
import re

def is_prime(num):
    """
     Checks if the number is prime or not
    """
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(first, last):
    """
     Finds all the primes and saves them to a list
    """
    primes = []
    for num in range(first, last + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_primes(primes):
    """
     Prints the list of primes
    """
    if len(primes) == 1:
        return str(primes[0])
    return ', '.join([str(n) for n in primes])

def get_first():
    """
     Gets the user's specified value first
    """
    first = 0.1
    while not isinstance(first, int):
        try:
            first = int(input("\nEnter the value you wish to start listing from: "))
        except ValueError:
            print("You must enter an integer! Please, try again.")
    return first

def get_last(first):
    """
     Gets the user's specified value last
    """
    last = 0.1
    while not isinstance(last, int):
        try:
            last = int(input("\nEnter the value you wish to end the listing at: "))
            check_value(first, last)
        except ValueError:
            print("You must enter an integer! Please, try again.")
        except AssertionError as error:
            print(f"{error} Please, try again.")
            last = 0.1
    return last

def check_value(first, last):
    """
     Checks if a < b
    """
    assert (first < last), f"The ending value cannot be equal to or less than the "\
        + "starting value, {first}!"

def get_option(choice):
    """
     Gets the user's choice for exiting the program
    """
    option = ""
    contain = False
    while not contain:
        try:
            option = input(f"\nDo you wish to {choice}? (Y/N)  ").upper()
            contain = check_option(option)
        except AssertionError as error:
            print(f"{error} Please, try again.")
    return "Y" in option

def check_option(option):
    """
     Checks if the user entered Y or N!
    """
    assert ("Y" in option or "N" in option), "You must enter Y or N!"
    return True

def save_primes(primes):
    """
     Saves results to a file if the user wishes to
    """
    save = get_option("save results to a file")
    if save:
        save_file = None
        while True:
            try:
                name = input("\nWhat name do you want to give to the results file? "\
                    + "(The file will be saved as a text file.) ")
                name = check_file_name(name)
                save_file = open(name, "w")
            except OSError as os_error:
                print("\n" + os_error.strerror + "! Please try again.")
            except AssertionError as error:
                print(f"\n{error} Please try again.")
            else: break
        save_file.write(primes)
        save_file.close()

def check_file_name(name):
    """
     Checks if the file name is vaild
    """
    assert (not re.search("[<>:/\\|?*]", name)), "Invalid file name!"
    return name + ".txt"

def prime_checker():
    """
     Runs the Prime Checker program
    """
    print("Welcome to Prime Checker!\nHere you can list all the primes for a "\
        + "specified range of values.")
    to_exit = False
    while not to_exit:
        first = get_first()
        last = get_last(first)
        primes = get_primes(find_primes(first, last))
        output = f"\nThe primes within the range of {first} and {last} are {primes}."
        print(output)
        save_primes(output.strip())
        to_exit = get_option("exit this program")
    print("\nGoodbye!")

# Main Program
prime_checker()
