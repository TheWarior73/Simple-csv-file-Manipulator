## Getting started
# Hi ! This script is here to prompt the user about differents elements about their database, it will let them edit it as freely as i possibly can make it be.
# ===( How to use )===
# You shouldn't even be there...
# ===( ••• )===

## Docstrings
# """Quick description of what the def does 
# Parameters : - param (1)
#              - param (2)
# Output : - what is given in output [Type]
# """ 


# = = = [Imports] = = =
from maths_stuff import get_possibilities
import time

# Code

def get_file() :
    """Prompt the user to chose a file wich is suposed to be a database following the csv format. (entry 1,entry 2,entry 3, ... , entry n)
    Parameters : - None (NoneType)
    Output : - FileName (str)"""
    print('Suported filetype can only be csv for some reasons.')
    filename = input('Filename // must be inside the script folder // ')
    filetype = '.csv'
    return str(filename+filetype)

# The database is an arborescence (meaning : entry 1 == main, entry 2 == submain etc...)

def get_main_entry(file_csv) :
    """Prompt the user to choose the main entry for their research/modification as well as showing them the possibilities
    Parameters : - [file_csv] the name of the file + the filetype (.csv)
    Output : - entry name (str)
             - determines if the user wish to create a new main file or not (Boolean)
    """
    # Vars
    temp_showing_list = []
    create_new = False

    # showing the possibilities
    possibility_list = get_possibilities(file_csv) # retrieve the possibilities from the file
    for i in range(len(possibility_list)) : 
        if possibility_list[i]['main'] not in temp_showing_list : # if the possibility is already shown, don't show it again.
            temp_showing_list.append(possibility_list[i]['main'])
            print(possibility_list[i]['main'])
    time.sleep(1)
    # Getting the desired entry
    get_entry = input('What is your main entry ? ')
    ## Need to add a safe check to determine if the given entry corespond to one in the possibilities (if not it will ask the user if they whant to create a new entry or if this was a typo)
    return str(get_entry) , create_new

