import os
import shutil
path = 'C:/Users/Sreekanth Murugan/Documents'
source = 'C:/Users/Sreekanth Murugan/Documents/C-99/ok.txt' 
destination = 'C:/Users/Sreekanth Murugan/Documents/C-99/ok(copy).txt'
dest = shutil.copy(source,destination)
print("after copying file:")
print(os.listdir(path)) 