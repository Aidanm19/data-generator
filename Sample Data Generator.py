#Sample Data Generator

import sys
import re

#Flag specifications
#   -fname      : first name
#   -lname      : last name
#   -name       : full name
#   -ip         : ip 
#   -date       : date
#   -timestamp  : timestamp
#   -num        : number (specify range?)
#   -bool       : boolean
#   -o          : output to file


def getInput():

    valid_flags = ["-fname", "-lname", "-name", "-ip", "-date", "-timestamp", "-num", "-bool", "-o"]

    flags = []

    #default values
    num = 1 
    rangeMin = 0
    rangeMax = 1000
    filename = None

    print("Welcome To The Data Generator\n")

    if len(sys.argv) > 1:

        #get the number of data to generate
        #this is always the last argument
        num = sys.argv[-1]                      

        for index, arg in enumerate(sys.argv):

            if (re.search("^-", arg) and arg in valid_flags):
                flags.append(arg)
                
                if arg == "-num":
                    try:
                        rangeMin = sys.argv[index+1]
                        rangeMax = sys.argv[index+2]

                        #check if range is valid
                    except Exception as e:
                        print(e)
                        print("Please enter a valid range")

                elif arg == "-o":
                    try:
                        filename =  sys.argv[index+1]

                    except Exception as e:
                        print(e)
                        print("Please enter a valid name")


    else:
        print("No flags or arguments entered")

    return flags, num, rangeMin, rangeMax, filename


def generate(flags_list, num, rangeMin, rangeMax, filename):

    json_output = {}
    return 

if __name__ == '__main__':
    print(getInput())
