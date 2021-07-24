# You can save variables in your Python programs to binary shelf files using the shelve module.
# This way, your program can restore data to variables from the hard drive. The shelve module will let
# you add Save and Open features to your program. For example, if you ran a program and entered some
# configuration settings, you could save those settings to a shelf file and then have the program load
# them the next time it is run.

import os
import shelve

newFileLocation = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\", "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Test1\\", "Shelve_Example\\", "mydata")
shelveFile = shelve.open(newFileLocation)
cats = ['Zophie', 'Pooka', 'Simon']
shelveFile['cats'] = cats
shelveFile.close()

# Reading data from Shelve
shelveFile = shelve.open(newFileLocation)
type(shelveFile)
print (shelveFile['cats'])
shelveFile.close()

# Reading data as keys and values
shelveFile = shelve.open(newFileLocation)
print (list(shelveFile.keys()))
print (list(shelveFile.values()))
shelveFile.close()

