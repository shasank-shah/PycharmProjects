import csv

unique_jobs = set()
age = []
with open('bank-data.csv', 'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(row)
            line_count += 1
        else:
            unique_jobs.add(row[1])
            age.append(row[0])

_ageDict = {'minAge': min(age), 'maxAge': max(age)}
profession = input("Enter the profession name: ")
while profession != "END":
    if profession.lower() in unique_jobs:
        print("The client is eligible to be approached for marketing campaign")
        for key, value in _ageDict.items():
            print("The " , key, " is ", value)
    else:
        print("The client is not eligible to be approached for marketing campaign")
    profession = input("Enter the profession name: ")