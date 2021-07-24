import os

# fileLocation = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\", "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Test1\\", "hello.txt")
# if os.path.exists(fileLocation):
#     #print (True)
#     helloFile = open(fileLocation)
#     helloContent = helloFile.read()
#     print (helloContent)

# newFileLocation = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\", "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Test1\\", "sonnet29.txt")
# if os.path.exists(newFileLocation):
#     sonnetFile = open(newFileLocation)
#     print (sonnetFile.readlines())

newFileLocation = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\", "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Test1\\", "bacon.txt")
baconFile = open(newFileLocation, 'w')
baconFile.write('Hello World!\n')
baconFile.close()
baconFile = open(newFileLocation, 'a')
baconFile.write('Bacon is not a vegetable\n')
baconFile.close()

baconFile = open(newFileLocation, 'r')
content = baconFile.read()
baconFile.close()
print (content)




