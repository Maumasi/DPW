
# List used to collect user generated responces
userMadLibList = []


print "Lets play some Mad Lib!"

# Function/Definition for Mad Lib responces and evaluation of responces
def madLib(list):

# Strings used to concatonate later
    pluralDays = ""
    pluralFood = ""

# This input is asked before the loop so that the list length is not null
    print "Name a country."
    userMadLibList.append(raw_input())

# while loop used until all inputs have been filled
    while len(list) != 5:

# for loop used in conjunction with while loop to evaluate if statement for all inputs
        for i in range(len(list)):
            if len(list) == 0:
                print "You didn't answer the first question! \n Name a country."
                list.append(raw_input())
            elif len(list) == 1:
                print "What's your name?"
                list.append(raw_input())
            elif len(list) == 2:
                print "Give me a number."

                num1 = raw_input()

# I used try/except to test if the instance is true or false.
# If I use an if/else statement I get an error.
                try:
                    isinstance(int(num1), int)
                    list.append(num1)
                except Exception:
                    print "You didn't give me a number."
                    pass

            elif len(list) == 3:
                print "What's your favorite food?"
                list.append(raw_input())
            elif len(list) == 4:
                print "Give me another number."

                num2 = raw_input()

                try:
                    isinstance(int(num2), int)
                    list.append(num1)
                except Exception:
                    print "You didn't give me a number."
                    pass

# if statments used to see if a plural word is needed by adding an "s" to the end of one of the
# list elements for each statement.
    if int(list[4]) > 1:
        pluralDays = "s"

    if int(list[2]) > 1:
        pluralFood = "s"

# The acctual Mad Lib string concatonated with the user generated answers from the if statement above.
    lib = "\nMad Lib:\nThere was a place that was very influenced by " + list[0] + ". \nThe people ate their food in the same way food was eaten in " + list[0] + ". \nOne day " + list[1] + " ate " + list[2] + " " + list[3] + pluralFood + ". " + list[1] + " was very ill for " + list[4] + " day" + pluralDays + " because of it. \n" + list[1] + ", has never eaten " + list[3] + " again."
    print lib
    return list

madLib(userMadLibList)

# A print out of the user generated answers in the order they were answered
print "\nHer are your responces in order:"
print "COUNTRY: " + userMadLibList[0] + "\nNAME: " + userMadLibList[1] + "\n1ST NUMBER: " + userMadLibList[2] + "\nFAVORITE FOOD: " + userMadLibList[3] + "\n2ND NUMBER: " + userMadLibList[4]


# ------ Lab 1: Mad Lib ------
#
# At least 2 strings
# At least 2 numbers
# And includes the following elements:
#
# One list/array
# One if statement with at least one logical operator
# One function
#   Must return a value
#   Must have and use parameters
# One loop


# And meet the following requirements:
#
# The mad lib's code must be well commented.
# Comments should explain code, not just label.
# All elements should have a purpose within the greater madlib.
# (In other words you can't create an array or function that isn't used)
# You must make required number meaningful commits to this file in your repository
# Any errors will earn an automatic ZERO on this assignment.
# Your mad lib should print out the entire story to the console.

# Mad Lib:
# There was a place were #COUNTRY changed the way people ate their food.
# One day #NAME ate #NUMBER1 #FOOD that made NAME very ill for #NUMBER2 days.
# #NAME , has never eaten #FOOD again.