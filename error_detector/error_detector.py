import csv

with open('key_without_reviews.csv', 'r') as t1, open('Insert_Filename.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('Insert_output.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)


file = open("Insert_output.csv")
reader = csv.reader(file)
lines = len(list(reader))

print("Number of incorrect output:", lines)
print("Accuracy: "+ str(((25000 - lines)/25000)*100) + " %")