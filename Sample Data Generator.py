#Sample Data Generator

#Libraries
import json
import sys
import re
import random
import csv

#Files
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


def getInput():

    flags = []

    #default values
    num = 1 
    rangeMin = 0
    rangeMax = 100
    filename = None

    #print("Welcome To The Data Generator\n")
    print(
        "  ________              ____        __                 \n"
        " /_  __/ /_  ___       / __ \____ _/ /_____ _          \n"
        "  / / / __ \/ _ \     / / / / __ `/ __/ __ `/          \n"
        " / / / / / /  __/    / /_/ / /_/ / /_/ /_/ /           \n"
        "/_/_/_/_/_/\___/    /_____/\__,_/\__/\__,_/            \n"
        "  / ____/__  ____  ___  _________ _/ /_____  _____     \n"
        " / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/     \n"
        "/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /         \n"
        "\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/          \n"
    )

    if len(sys.argv) > 1:

        #get the number of data to generate
        #this is always the last argument
        num = sys.argv[-1]                      

        for index, arg in enumerate(sys.argv):

            if (re.search("^-", arg)):
                flags.append(arg)
                
                #special cases for flags
                if arg == "-num" and sys.argv[index+1] < sys.argv[index+2]:
                    try:
                        rangeMin = sys.argv[index+1]
                        rangeMax = sys.argv[index+2]

                    except Exception as e:
                        print(e)
                        print(f"Error with range, using default values")

                elif arg == "-o":
                    try:
                        filename = sys.argv[index+1]

                    except Exception as e:
                        print(e)
                        print("Please enter a valid name")

            elif re.search("^-", arg):
                print(f'Error: flag {arg} not recognized\n')
    else:
        print("No flags or arguments entered")

    return flags, num, rangeMin, rangeMax, filename
    

def generateDate():
    #ISO 8601 --> YYYY-MM-DD

    year_min = 1800
    year_max = 2025

    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    month = random.randint(1, 12)

    if month == 2:
        day = random.randint(1, 28)
    elif month in months_with_31_days:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    
    year = random.randrange(year_min, year_max)

    return f'{year}-{month}-{day}'


def generateTimestamp():

    #ISO 8601 --> YYYY-MM-DD HH:mm:ss
    date = generateDate()
    time = f'{random.randint(0, 24)}:{random.randint(0, 60)}:{random.randint(0, 60)}'

    return f'{date}T{time}'


def generateUID():
    return


def generateUsername():

    fname = random.choice(names.fnames)
    lname = random.choice(names.lnames)
    num = random.randint(1, 9999)

    numChars_fname = random.randint(1, len(fname))
    numChars_lname = random.randint(0, len(lname))
    num_digits = random.randint(0, 4)

    uname = f'{fname[:numChars_fname]}{lname[:numChars_lname]}{str(num)[:num_digits]}'
    if len(uname) < 4:
        
        for i in range(len(uname)):
            uname = uname + chr(random.randrange(65, 90))       #add random uppercase letters if uname is not long enough

    return uname


def generate(flags_list, rangeMin, rangeMax):

    json_output = {}

    for flag in flags_list:

        if flag == "-fname":
            json_output['first_name'] = random.choice(names.fnames)

        elif flag == '-lname':
            json_output['last_name'] = random.choice(names.lnames)

        elif flag == '-name':
            json_output['full_name'] = f'{random.choice(names.fnames)} {random.choice(names.lnames)}'

        elif flag == '-ip':
            json_output['ip'] = f'{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'

        elif flag == '-date':
            json_output['date'] = generateDate()

        elif flag == '-timestamp':
            json_output['timestamp'] = generateTimestamp()

        elif flag == '-bool':
            json_output['boolean'] = random.randint(0, 1) == 0

        elif flag == '-num': 
            json_output['number'] = random.randrange(int(rangeMin), int(rangeMax))

        elif flag == '-uname':
            json_output['username'] = generateUsername()

    return json_output


def generateOutput():

    flags, num, rangeMin, rangeMax, filename = getInput()

    #print([flags, num, rangeMin, rangeMax, filename])

    if (len(flags) == 0):
        return

    output = {"sample_data":[]}

    for i in range(int(num)):

        json_object = generate(flags, rangeMin, rangeMax)
        output['sample_data'].append(json_object)
    
    if filename != None:    #write to file

        file_format = filename.split('.')[1]
        path = f'/Users/aidanm/Desktop/{filename}'

        #Write JSON File
        if file_format == 'json':

            with open(path, 'w') as json_file:
                json.dump(output, json_file, indent=4)      #indent 4 does prety print

            return


        elif file_format in ['yaml', 'yml']:
            pass


        elif file_format == 'csv':

            with open(path, 'w', newline='') as csv_file:

                fieldnames = []
                keys = output['sample_data'][0].keys()
                for key in keys: 
                    fieldnames.append(key)

                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for data in output['sample_data']:
                    writer.writerow(data)
                    
            return    

    else:   #print to terminal

        output_pretty = json.dumps(output, indent=4)
        print(output_pretty)

    return


if __name__ == '__main__':    
    generateOutput()

    """
                keys = output['sample_data'][0].keys()
                keys_str = ''
                for key in keys: keys_str = keys_str + key + ','
                print(keys_str.strip(','))

                for jsonObj in output['sample_data']:
                    data_str = ''

                    for data in jsonObj.values():
                        #print(data)
                        data_str = data_str + data + ','
                
                    print(data_str.strip(','))
                """