def IsYearLeap(year):
    #
    if (year % 4 > 0) and (year % 400 > 0):
        return False
    elif (year % 100 > 0):
        return True
    else:
        return True


#

testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]
for i in range(len(testdata)):
    yr = testdata[i]
    print(yr, "->", end="")
    result = IsYearLeap(yr)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")
