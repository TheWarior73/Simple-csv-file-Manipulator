## Getting started
# Hi ! This script is here to get all the mess together and create a somewhat working software

# * * * ( How to use ) * * *
# Execute the file and get going !
# you will be prompted to choose between 2 modes, one will run the program in the console, the other one in a graphic interface.
# * * * ( ••• ) * * * 

## = = = ( CAUTION ) = = =
#
# This file contains auto executing code !
# DO NOT EXECUTE IT if unsure about the code present in the file
#
# = = = ( /!\ /!\ ) = = =


## Docstrings
# """Quick description of what the def does 
# Parameters : - param (1)
#              - param (2)
# Output : - what is given in output [Type]
# """ 

# = = = [Imports] = = =
import prompt
import maths_stuff

# = = = [Code] = = =

## The actual stuff
def app_console() :
    """This function takes all the bits and bobs around the files to put them together and show a somewhat understandable thing
    Paramenets : - None (N/A)
    Output : - exit code [debbuging and informational] (str or int)
    """
    # Vars
    exitcode = ''
    file = ''

    # ===
    print('Hi ! This is the console Version of this csv file manipulator. \nPlease start by selecting your file \nRemember, it should be in the same folder as this script.\n')
    file = prompt.get_file()
    print("Ok let's see what we have in there ! \n")
    main_entry = prompt.get_entry(file)
    if main_entry == 'retry' : # retry in case of fail to obtain the entry.
        print('Well, try again ! What entry do you want to acess ?')
        main_entry = prompt.get_entry(file)

    return exitcode


def app_Ui_edition() :
    """ This function does the same as app_console() expect it will not run in the console but in a dedicated window.
    Parameters : - None (N/A)
    Output : exit code [debbug & informations] (str or int)
    """
    # Vars
    exitcode = ''

    # ===


    return exitcode


## Auto executing code when executing the file
app_version = input('Console or Windowed version ? \nType C or W for short')
if app_version == 'C' or app_version == 'c' :
    app_console()
elif app_version == 'W' or app_version == 'w' :
    app_Ui_edition()

# = = = [END OF FILE] = = =