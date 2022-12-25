import os
import shutil
from_dir = 'C:/Users/Admin/Downloads'
to_dir = 'C:/Users/Admin/Desktop/Downloadimage'
list_of_file = os.listdir(from_dir)
print(list_of_file)
for file_name in list_of_file:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension =='':
      continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
      path1 = from_dir + '/' + file_name,
      path2 = to_dir + '/' + 'image_file',
      path3 = from_dir + '/' +'image_file' + '/' + file_name
    if os.path.exists(path2):
        print('moving'+ file_name)
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print('moving'+ file_name)
        shutil.move(path1,path3)


