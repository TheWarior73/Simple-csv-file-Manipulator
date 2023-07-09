## Getting started
# Hi ! This script is here to prompt the user about differents elements about their database, it will let them edit it as freely as i possibly can make it be.

# * * * ( How to use ) * * *
# You shouldn't even be there...
# * * * ( ••• ) * * *

## Docstrings
# """Quick description of what the def does 
# Parameters : - param (1)
#              - param (2)
# Output : - what is given in output [Type]
# """ 


# = = = [Imports] = = =
from maths_stuff import get_possibilities
import time

# = = = [Code] = = =

def get_file() :
    """Prompt the user to chose a file wich is suposed to be a database following the csv format. (entry 1,entry 2,entry 3, ... , entry n)
    Parameters : - None (NoneType)
    Output : - FileName (str)"""
    print('Suported filetype can only be csv for some reasons.')
    filename = input('Filename // must be inside the script folder // ')
    filetype = '.csv'
    return str(filename+filetype)

# The database is an arborescence (meaning : entry 1 == main, entry 2 == submain etc...)

def get_entry(file_csv:str,lvl=0) :
    """Prompt the user to choose the main entry for their research/modification as well as showing them the possibilities
    Parameters : - [file_csv] the name of the file + the filetype (.csv)
                 - [lvl] the level to look at [default at 0] (int)
    Output : - entry name (str)
             - determines if the user wish to create a new main file or not (Boolean)
    """
    # Vars
    temp_showing_list = []
    create_new = False

    ## = = = [levels] = = =
    # opening the file in read mode
    file = open(file_csv, 'r')
    content = [] # contains all the file in list form
    for line in file : # getting every line in the file
        content.append(line.strip().split(','))
    file.close
    indexes = (content[0]) # gets the element on the first line to correctly label everything
    lvl_content = indexes[lvl] # gets the str of the lvl to search the list.
    ## = = = {levels} = = =

    # console version log
    print('Below is the possibility list for the main element or your list \n')
    # showing the possibilities
    possibility_list = get_possibilities(file_csv) # retrieve the possibilities from the file
    for i in range(len(possibility_list)) : 
        if possibility_list[i][lvl_content] not in temp_showing_list : # if the possibility is already shown, don't show it again.
            temp_showing_list.append(possibility_list[i][lvl_content])
            print(possibility_list[i][lvl_content])
    time.sleep(1)
    # Getting the desired entry
    get_entry = input('What is your main entry ? ')
    # Safecheck for spelling errors & creation of new entry otherwise.
    if get_entry not in temp_showing_list : # if the entry given before does not apear in the list, do the following bellow :
        print('\n- You asked for a name not registered, check your spelling or maybe \nwould you like to create a new main entry using this name ? (' + get_entry + ')')
        create_new_str = input('Yes/No') # typing anything else than Yes | yes | y | Y will just make the user retry.
        if create_new_str == 'Yes' or create_new_str == 'yes' or create_new_str == 'y' or create_new_str == 'Y':
            create_new = True
        else :
            return 'retry' # will let the function that uses it know that the program could not resolve a name and therefore it should retry asking the user.
    return str(get_entry) , create_new

