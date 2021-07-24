# Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz
# on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students
# not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it
# impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a
# lengthy and boring affair. Fortunately, you know some Python.

import os
import datetime
import random
import linecache

filename = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\",
                        "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Quiz\\", "Questions.qst")


def lineCount(filename):
    # f = open(filename, 'r')
    with open(filename) as foo:
        lines = len(foo.readlines())
        # print ('No of Lines: ', lines)
        return lines


lineCountQuesFile = lineCount(filename)
print('No of lines: ', lineCountQuesFile)


def questionNo(filename):
    f = open(filename, 'r')
    return linecache.getline(f, 1)
    # lines = f.readlines()
    # for questionLines in lineCountQuesFile:
    #     question = lines[questionLines]
    #     return question
    # rdnQuestionNo = random.randint(1, 3)
    # if (rdnQuestionNo == 1):
    #     question = lines[rdnQuestionNo]


print('Question is: ', questionNo(filename))


# folder = "D:\\Shasank\\NLG\\Python_Projects\\Automate_The_Boring_Stuff\\Automate_the_Boring_Stuff_onlinematerials\\Chapter_8_Files\\Quiz"
# if os.path.exists(folder):
#     newFolder = datetime.datetime.today().strftime("%Y") + datetime.datetime.today().strftime("%m") + datetime.datetime.today().strftime("%d") + "_" + datetime.datetime.today().strftime("%H") + datetime.datetime.today().strftime("%M") + datetime.datetime.today().strftime("%S") + "_" + datetime.datetime.today().strftime("%f")
# os.makedirs(os.path.join(folder, newFolder))

# print (True)

