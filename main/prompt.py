## Getting started
# Hi ! This script is here to prompt the user about differents elements about their database, it will let them edit it as freely as i possibly can make it be.
# ===( How to use )===
# Yet to be defined 
# ===( ••• )===

## Docstrings
# """Quick description of what the def does 
# Parameters : - param (1)
#              - param (2)
# Output : - what is given in output [Type]
# """ 


# Imports



# Code

def get_file() :
    """Prompt the user to chose a file wich is suposed to be a database following the csv format. (entry 1,entry 2,entry 3, ... , entry n)
    Parameters : - None (NoneType)
    Output : - FileName (str)"""
    filename = input('Filename // must be inside the script folder // ')
    filetype = input('FileType // csv | ... | ... // ')
    return str(filename), str(filetype)

# The database is an arborescence (meaning : entry 1 == main, entry 2 == submain etc...)

def get_main_entry() :
    """Prompt the user to choose the main entry for their research/modification as well as showing them the possibilities
    Parameters : 
    Output : entry name (str)
    """
    # Vars

    # showing the possibilities
    print( 'Function yes to be implemented (showing possibilities)' )
    # Getting the desired entry
    get_entry = input('What is your main entry ? ')
    ## Need to add a safe check to determine if the entry given corespond to one in the possibilities (if not it will ask the user if they whant to create a new entry or if this was a typo)
    return str(get_entry)

