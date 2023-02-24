import stdio
import sys
import random
import stdarray
import stdaudio
import math

SPS=44100
CONCERT_A=440.0

while not stdio.isEmpty():
    pitch=stdio.readInt()
    duration=stdio.readFloat()
    hz=CONCERT_A*(2**(pitch/12.0))
    n=int(SPS*duration)
    samples=stdarray.create1D(n+1,0.0)
    for i in range(n+1):
        samples[i]=math.sin(2.0*math.pi*i*hz/SPS)
    stdaudio.playSamples(samples)
stdio.wait()