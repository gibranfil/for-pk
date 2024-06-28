import glob
import os
from pathlib import Path
def glob_data (root_dir) :
    list_data = None
    empty_return = []
    for root, dirs,filename in os.walk(root_dir):
        
        #print(f'Current directory: {root}')
        #print (dirs)
        list_data = dirs
        break

    #print (len(list_data))
    for folder in dirs:
        result = glob.glob (f'{os.path.join(root_dir, folder)}/*')
        empty_return.append (result)
    
    return empty_return, list_data
    

def create_directories(folder_names, directory):
    for folder in folder_names:
        try:
            os.makedirs(os.path.join(directory, folder))
            print(f"Directory '{folder}' created successfully.")
        except FileExistsError:
            print(f"Directory '{folder}' already exists.")


def read_string (text) :
    
    text = Path(text).stem
    result  = text.split("_")
    result = result [:-1]
    if len (result) != 3 :
        firstWord = text.split(' ', 1)[0]
        result.append (firstWord)

    return result
    




