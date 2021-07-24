#Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz
# on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students
# not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it
# impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a
# lengthy and boring affair. Fortunately, you know some Python.

import os
import datetime
import random
import linecache
import string
import pickle

folder = "D:\\Shasank\\NLG\\Python_Projects\\Automate_The_Boring_Stuff\\Automate_the_Boring_Stuff_onlinematerials\\Chapter_8_Files\\Quiz"
filename = os.path.join("D:\\", "Shasank\\", "NLG\\", "Python_Projects\\", "Automate_The_Boring_Stuff\\", "Automate_the_Boring_Stuff_onlinematerials\\", "Chapter_8_Files\\", "Quiz\\", "Questions.qst")

def lineCount(filename):
    with open(filename) as foo:
        totalLines = len(foo.readlines())
        return totalLines
totalLineCount = lineCount(filename)

if os.path.exists(folder):
    rollNo = 0
    for i in range(totalLineCount):
        # str = i
        rollNo = rollNo + 1
        if rollNo <= totalLineCount:
            questionPaper = 'Paper_' + str(rollNo).strip() + '.txt'
            newQuestionPaper = os.path.join(folder, questionPaper)
            lst = list(range(1, totalLineCount))
            addElement = max(lst) + 1
            lst.append(addElement)
            random.shuffle(lst)
            theFile = open(newQuestionPaper, 'a')
            quesNo = 1
            for indx in lst:
                shuffledQuestions = linecache.getline(filename, indx)
                formattedQuestions = str(quesNo) + ") " + shuffledQuestions + "\n"
                theFile.write("%s" %formattedQuestions)
                quesNo = quesNo + 1
            theFile.close
        else:
            exit ;