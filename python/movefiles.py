import os
import shutil

destination_file = './dest/'
download_path = 'C:\\Users\\BitaraPC\\Downloads\\'

files = []

# for file in os.listdir(download_path):
#     name, extension = os.path.splitext(file)
#     print(file)   
#     if extension == '.txt':
        # files.append(name)
        # shutil.move(name, destination_file)

for file in os.listdir(download_path):
    filepath, x = os.path.splitext(download_path)
    filename, extension = os.path.splitext(file)
    
    if extension == '.txt':
        print(filepath + filename)
        shutil.move(filepath + filename + extension, destination_file)        
