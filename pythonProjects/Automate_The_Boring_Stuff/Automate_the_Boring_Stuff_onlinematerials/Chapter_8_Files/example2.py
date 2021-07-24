#To Find size of complete folder only with files.
import os

folder_location = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\", "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Test1")
#print (folder_location)
totalSize = 0

for filename in os.listdir(folder_location):
    #print (filename)
    folder_fileName = os.path.join(folder_location,filename)
    #print (folder_fileName)
    if os.path.isfile(folder_fileName):
        print (folder_fileName)
        totalSize = totalSize + os.path.getsize(folder_fileName)

print (totalSize)