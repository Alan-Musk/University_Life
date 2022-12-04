import sys

numbers=[1,2,4,6,7,84,8,0]

if 0 in numbers:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)