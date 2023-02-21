import stdio
import sys
import math

if len(sys.argv)!=3:
    stdio.writeln('参数错误')
else:
    try:
        num = int(sys.argv[1])
        base = int(sys.argv[2])
        if base < 2 or base > 16:
            print("Base must be between 2 and 16")
        else:
            digits="0123456789ABCDEF"
            res=""
            while num>0:
                res=digits[num%base]+res
                num //=base
        stdio.writeln(res)
    except ValueError:
            print("Invalid input. Please enter a valid number and base.")
