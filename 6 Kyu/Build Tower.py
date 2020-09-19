# Description:
# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# 
# Tower block is represented as *
# 
# Python: return a list;
# Have fun!
# 
# for example, a tower of 3 floors looks like below
# 
# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]
# and a tower of 6 floors looks like below
# 
# [
#   '     *     ', 
#   '    ***    ', 
#   '   *****   ', 
#   '  *******  ', 
#   ' ********* ', 
#   '***********'
# ]

def tower_builder(n_floors):
    new_list = []
    for i,val in reversed(list(enumerate(reversed(range(0, n_floors))))):
        new_list.append(" "*(i) + "*"*(1+val*2) + " "*(i))
    return new_list
