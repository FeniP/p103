import os
import shutil
source="C:/Users/mahif/Downloads/abc"
destination="C:/Users/mahif/OneDrive/Desktop"
files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    if ext == '':
        continue
    if ext in [ ‘.txt’, ‘.doc’, ‘.docx’, ‘.pdf’’]:
        path1 = source + '/' + i
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "Document_Files" + '/' + i
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("creating and moving")
            shutil.move(path1,path3)
