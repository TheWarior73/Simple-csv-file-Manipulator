## Getting started
# Hi ! This script is here to do all the *complicated* maths stuff for the scripts.
# ===( How to use )===
# You shouldn't even be there...
# ===( ••• )===

## Docstrings
# """Quick description of what the def does 
# Parameters : - param (1)
#              - param (2)
# Output : - what is given in output [Type]
# """

# Imports
import prompt


# Code  


def get_possibilities(file,start_lvl,lvl=0) :
    """This function retrieves the different possibilities for a given level of informations.
    Parameter : - [file] the file where the function will look for informations.
                - [start_lvl] the level where you start (eg: want to see stuff in main1;sub1, useless to see stuff in main2;sub1 )
                - [lvl] level of information to look at (int) default at 0.
    Output : A list formed of p-uplets (list)
    """
    # opening the file in read mode
    file = open(file + '.csv', 'r')
    content = [] # contains all the file in list form
    for line in file : # getting every line in the file
        content.append(line.strip().split(','))
    file.close

    # getting the required level
    contentlvl = [] # contains the demanded informations.
    for i in range(len(content)) :
        contentlvl.append(content[i][lvl])

    return contentlvl