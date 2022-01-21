from datetime import date
import math
import os
import sys


def promptInvalidEntry(message):
    # Clear shell
    os.system('cls' if os.name == 'nt' else 'clear')
    print(message)
    getDate("")


def printAge(years, days, months, daysSinceBirth):
    response = "Das Alter ist {} Jahre {} Monate und {} Tage, das sind {} Tage".format(
        years, months, days, daysSinceBirth)

    print(response)


def getDate(argument):

    if(argument == ""):
        print("Enter the date in the following format: dd.mm.yyyy")
        text = input("").split(".")
    else:
        text = argument.split(".")

    if(len(text[2]) < 4):
        promptInvalidEntry("Invalid Entry")
        return

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

    years = math.floor(days / 365)
    months = math.floor(days % 365 / 30.47)
    daysLeft = round(days % 365 % 30.47)

    printAge(years, daysLeft, months, days)


if(len(sys.argv) > 1):
    getDate(sys.argv[1])
