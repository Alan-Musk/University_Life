import random
import stdio

RANGE=1000000

secret=random.random(1,RANGE+1)
stdio.write('I am thinking of a secret number between 1 and')
stdio.writeln(RANGE)

guess=0
while guess != secret:
    stdio.writeln('What is your guess?')
    guess=stdio.readInt()
    if(guess<secret):stdio.writeln('Too low')
    elif (guess>secret):stdio.writeln('Too high')
    else: stdio.writeln('You Win!')

