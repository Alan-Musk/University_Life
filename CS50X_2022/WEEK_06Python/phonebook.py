import csv
from cs50 import get_string

file=open("Phonebook.csv","a")

name=get_string("Name:")
number=get_string("Numbers:")

writer=csv.writer(file)
writer.writerow([name,number])

file.close() 