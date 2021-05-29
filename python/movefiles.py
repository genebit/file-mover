import os
import shutil

destination_file = './dest/'
download_path = 'C:\\Users\\BitaraPC\\Downloads\\'

for file in os.listdir(download_path):
    path, x = os.path.splitext(download_path)
    name, extension = os.path.splitext(file)
    
    if extension == '.txt':
        absolute_path = path + name + extension
        shutil.move(absolute_path, destination_file + 'txt/')        
