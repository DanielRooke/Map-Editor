#File Reader
from objects import MapSave

"""reader will need to return give a platform and a length || mutate global vairables which i would rather not do
"""


def read_file(path):
    '''read_file(path) -> MapSave()
    read a map txt file and return a MapSave object.
    return None if ad error is encountered'''
    file = open(path)
    save = MapSave(path)
    #check each line
    if file[0] == 'APPLICATION MAP\n':
        for line in file:
            #lines representing map blocks
            if line[0] in '0123456789':
                line.strip('\n')
                for char in line:
                    save.add_block(char)
            #find lines displaying start and end postions for moving blocks
            elif line.startswith('('):
                #(x1, y1),(x2, y2)
                pass
        return save
    else:
        #false first line case
        print('ERROR: NOT A MAP FILE')
        return None