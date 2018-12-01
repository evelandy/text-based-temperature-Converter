#!/usr/bin/env python3
"""evelandy/W.G.
Nov. 29 2018 7:16pm
text-based-temperature-converter
Python36-32 
"""
def celsius(fahr):
    return "{} degrees fahrenheit converted is {} degrees celsius".format(temp, int((5 / 9) * (fahr - 32)))


def fahrenheit(cel):
    return "{} degrees celsius converted is {} degrees fahrenheit".format(temp, round((9 / 5) * cel + 32, 2))


while True:
    try:
        temp = float(input("\nWhat is the temperature you want to convert? "))
        print("What would you like to convert your temperature to?\nF) Fahrenheit\nC) Celsius")
        choice = input(": ")
        if choice.lower() == 'f':
            print(fahrenheit(temp))
            print("Would you like to check another temperature?\nY) Yes\nN) No")
            ans = input(": ")
            if ans.lower() == 'y' or ans.lower() == 'yes':
                continue
            elif ans.lower() == 'n' or ans.lower() == 'no':
                print("Thank you, please come back soon!")
                break
            elif ans.lower() != 'y' or ans.lower() != 'yes' and ans.lower() != 'n' or ans.lower() != 'no':
                print("Sorry that's not a valid choice... Terminating...")
                break
        elif choice.lower() == 'c':
            print(celsius(temp))
            print("Would you like to check another temperature?\nY) Yes\nN) No")
            ans = input(": ")
            if ans.lower() == 'y' or ans.lower() == 'yes':
                continue
            elif ans.lower() == 'n' or ans.lower() == 'no':
                print("Thank you, please come back soon!")
                break
            elif ans.lower() != 'y' or ans.lower() != 'yes' and ans.lower() != 'n' or ans.lower() != 'no':
                print("Sorry that's not a valid choice... Terminating...")
                break
        else:
            print("The ONLY choices are:\nF) for Fahrenheit, and \nC) for Celsius \nPLEASE choose one of those...")
    except ValueError:
        print("\nA letter is NOT a temperature, Please enter digit values for the temperature\n")
