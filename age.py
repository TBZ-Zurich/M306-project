from datetime import date
import math
import os
import sys

# Clears the terminal and prints an error message. Also the user gets a message shown


def promptInvalidEntry(message):
    # Clear shell
    os.system('cls' if os.name == 'nt' else 'clear')
    print(message)
    getDate("")

# Prints the information to the terminal


def printAge(years, days, months, daysSinceBirth):
    response = "Das Alter ist {} Jahre {} Monate und {} Tage, das sind {} Tage".format(
        years, months, days, daysSinceBirth)

    print(response)

# This method takes the argument "argument", this has a value when a argument is given when the script is called. Else it is ""


def getDate(argument):

    # When date is not in command this statement gets the data via a prompt on the terminal
    if(argument == ""):
        print("Enter the date in the following format: dd.mm.yyyy")
        text = input("").split(".")
    else:
        text = argument.split(".")

    # Years that are not full are not allowed ex. 09 is not good 2009 is good
    if(len(text[2]) < 4):
        promptInvalidEntry("Invalid Entry")
        return

    # Try catch to catch when someone enters a date that does not exist ex. 29th february 2005
    try:
        calculateAge(date(int(text[2]), int(text[1]), int(text[0])))
    except:
        promptInvalidEntry("Invalid Entry - date may not exist")


def calculateAge(birthDate):

    today = date.today()

    age = today - birthDate

    days = age.days

    if(days < 0):
        promptInvalidEntry(
            "You can't use a computer when you are not born yet :)")

    # values get rouded down since you need to live 18 years to be 18 and not 17.5 years
    years = math.floor(days / 365.2425)

    # Same here jus with months
    months = math.floor(days % 365.2425 / 30.47)

    # This value is not perfectly accurate due to viewpoint of year / month
    daysLeft = round(days % 365.2425 % 30.47)

    printAge(years, daysLeft, months, days)


# checks if arguments match
if(len(sys.argv) > 1):
    getDate(sys.argv[1])
else:
    getDate("")
