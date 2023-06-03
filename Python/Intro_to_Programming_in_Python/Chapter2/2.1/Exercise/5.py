import math
import stdio

def sigmoid(x):
    return 1/(1+math.exp(-x))

stdio.writeln(sigmoid(1))