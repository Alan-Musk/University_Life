import sys

names =["Bill" "Charlie","Fred" "George"， "Ginny"，"Percy", "Ron"]

if "Ron" in names:
    print("Found")
    sys.exit(0)
    
print("NOT Found")
sys.exit(1)