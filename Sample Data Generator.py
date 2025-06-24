#Sample Data Generator

import json
import sys
import re
import random

import names

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


fnames_list = ['Joe', 'Bob', 'Alice']
lnames_list = ['Doe', 'Brown', 'Smith']


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


def generateIp():
    return f'{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'


def generate(flags_list, rangeMin, rangeMax, filename):

    json_output = {}

    for flag in flags_list:

        if flag == "-fname":
            json_output['first_name'] = random.choice(names.fnames)

        elif flag == '-lname':
            json_output['last_name'] = random.choice(names.lnames)

        elif flag == '-name':
            json_output['full_name'] = f'{random.choice(names.fnames)} {random.choice(names.lnames)}'

        elif flag == '-ip':
            json_output['ip'] = generateIp()

        elif flag == '-date':
            json_output['date'] = ''

        elif flag == '-timestamp':
            json_output['timestamp'] = ''

        elif flag == '-bool':
            json_output['boolean'] = ''

    return json_output



if __name__ == '__main__':
    flags, num, rangeMin, rangeMax, filename = getInput()

    for i in range(int(num)):

        output = generate(flags, rangeMin, rangeMax, filename)
        print(output)
    
    