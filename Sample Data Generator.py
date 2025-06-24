#Sample Data Generator

import json
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


def match_flags(flags_list):

    json_output = {}

    for flag in flags_list:

        if flag == "-fname":
            json_output['first_name'] = ''

        elif flag == '-lname':
            json_output['last_name'] = ''

        elif flag == '-name':
            json_output['full_name'] = ''

        elif flag == '-ip':
            json_output['ip'] = ''

        elif flag == '-date':
            json_output['date'] = ''

        elif flag == '-timestamp':
            json_output['timestamp'] = ''

        elif flag == '-bool':
            json_output['boolean'] = ''

    return json_output




def generate(json_output, num, rangeMin, rangeMax, filename):


    return 



if __name__ == '__main__':
    flags, num, rangeMin, rangeMax, filename = getInput()

    output = match_flags(flags)

    print(output)

