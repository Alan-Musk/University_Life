import stdio
import sys

stdio.write("Hey,")
stdio.write(sys.argv[1]+"  How are you")
# When the user inputed @!&^%,out:zsh: event not found: &
# When the user inputed python 5 Bob, the program output Can't open
# When the user inputed 5.py Bob,the program output  conmand not found:5.py
# When the user inputed python3 5.py Alice Bob, the program only output "Alice"