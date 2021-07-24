#To Find size of complete folder with files and sub directories files.
import os

folderLocation = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\", "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Test1")
#print (parentFolder)

def getFiles(folderLocation):
    totalSize  = os.path.getsize(folderLocation)
    print (folderLocation)
    print (totalSize)
    #exit ()
    for file in os.listdir(folderLocation):
        indFile = os.path.join(folderLocation, file)
        if (os.path.isfile(indFile)):
            print (indFile)
            totalSize += os.path.getsize(indFile)
        elif (os.path.isdir(indFile)):
            totalSize += os.path.getsize(indFile)
            getFiles(indFile)
        print("Total Size: ", totalSize)
    return totalSize
    #return totalSize
getFiles(folderLocation)
#print ("The ", folderLocation, " size is: ", str(getFiles(folderLocation)))
