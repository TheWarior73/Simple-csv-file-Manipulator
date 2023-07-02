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

# = = = [Imports] = = =


# Code  

def get_possibilities(file: str,start_main: str = '',lvl=1) :
    """This function retrieves the different possibilities for a given level of informations.
    Parameter : - [file] the file where the function will look for informations.
                - [start_main] (int) the level where you start (eg: want to see stuff in main1;sub1, useless to see stuff in main2;sub1 )
                - [lvl] level of information to look at (int) default at 1.
    Output : A list formed of tuples (list)
    """
    ## opening the file in read mode
    file = open(file, 'r')
    content = [] # contains all the file in list form
    for line in file : # getting every line in the file
        content.append(line.strip().split(','))
    file.close

    ## ===(creating the list )===
    # vars for creating a tuple.
    indexes = (content[0]) # gets the element on the first line to correctly label everything
    data = [] # where everything is stocked
    tempo = {} # temporary tuple, resets every i iteration.
    # ===
    if str(start_main) == '' :              # = = = [ If the start main is empty, show everything ] = = =
        for i in range(len(content)-1) : # we get every line except the first one.
            for j in range(len(content[0])) : # we get every element per line
                tempo[indexes[j]] = content[i+1][j] # creating the tuple w/ the indexes values
            
            # checking for empty tuples (exept for the last one, done at the end)
            for check in range(len(data)) :
                if str(data[check]) == '{}' :
                    data.remove(data[check])
                    check -= 1
            # ===(end of check)===

            data.append(tempo)
            tempo = {}

    else :                                          # = = = [ Else show the requested entries ] = = =
        for i in range(len(content)-1) : # we get every line except the first one.
            for j in range(len(content[0])) : # we get every element per line
                if content[i+1][0] == start_main :
                    tempo[indexes[j]] = content[i+1][j] # creating the tuple w/ the indexes values

            # checking for empty tuples (exept for the last one, done at the end)
            for check in range(len(data)) :
                if str(data[check]) == '{}' :
                    data.remove(data[check])
                    check -= 1
            # ===(end of check)===

            data.append(tempo)
            tempo = {}

    # check for last element
    if str(data[-1]) == '{}' :
        data.remove(data[-1])
    return data
