#writes save to a .txt file
from objects import MapSave

def write_file(filePath, save):
    '''write_file(path, MapSave) -> None
    write the string version of MapSave to a txt at path'''
    #check if file pre exists (write or overwrite)
    file = open(filePath, 'w')
    #writei the string version of save to the file
    file.write(str(save))
    #close txt
    file.close()
    save.save()