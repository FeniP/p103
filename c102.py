import os
import shutil
path= os.getcwd()
print(path)
#os.mkdir("abc")
files=os.listdir("C:/Users/mahif/Downloads")
print(files)
path1=os.path.exists("C:/Users/mahif/Downloads/abc")
print(path1)
name,ext=os.path.splitext("C:/Users/mahif/Downloads/trex_3.png")
print(name)
print(ext)
source="C:/Users/mahif/Downloads/abc"
destination="C:/Users/mahif/OneDrive/Desktop"
files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    if ext == '':
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Image_Files"
        path3 = destination + '/' + "Image_Files" + '/' + i
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("creating and moving")
            shutil.move(path1,path3)

