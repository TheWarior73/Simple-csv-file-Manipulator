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
# Output : - what is given in output [Type]*
#
# - * : optional
# """ 

# = = = [ Exit codes ] = = =
# [1] | 'Not yet implemented'
# As said here, not much to add expect that I'm working on it, or at least I should (I don't mind being reminded of it tho)
#
# [2] | 
#
#
# [3] |
#
#

# = = = [Imports] = = =
import prompt
#import maths_stuff

# = = = [Code] = = =

## The actual stuff
def app_console() :
    """This function takes all the bits and bobs around the files to put them together and show a somewhat understandable thing
    Parameters : - None (N/A)
    Output : - exit code [debugging and informational] (str or int)
    """
    # Vars
    exitcode = ''

    # ===
    print('Hi ! This is the console Version of this csv file manipulator. \nPlease start by selecting your file \nRemember, it should be in the same folder as this script.\n')
    file = prompt.get_file() # obtaining the file.
    print("Ok let's see what we have in there ! \n")
    main_entry = prompt.get_entry(file) # getting the main entry
    if main_entry == 'retry' : # retry in case of fail to obtain the entry.
        print('Well, try again ! What entry do you want to access ?')
        while main_entry == 'retry' :
            main_entry = prompt.get_entry(file)
    if main_entry[1] : # attempting to create a new main entry.
        exitcode = '[1] | Check the [ Exit codes ] section for more information' # TEMPORARY while the crate a new entry block is under development.

    # exitcode if return doesn't show up
    print('exitcode :\n' )
    return exitcode


def app_Ui() :
    """ This function does the same as app_console() expect it will not run in the console but in a dedicated window.
    Parameters : - None (N/A)
    Output : exit code [debug & information] (str or int)
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
    app_Ui()

# = = = [END OF FILE] = = =