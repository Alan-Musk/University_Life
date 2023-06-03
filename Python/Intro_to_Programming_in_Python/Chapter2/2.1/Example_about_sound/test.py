import stdarray
import math
import stdio
import stdaudio

# 声波计算
def tone(hz,duration,sps=44100):
    n=int(sps*duration)
    a=stdarray.create1D(n+1,0.0)
    for i in range(n+1):
        a[i]=math.sin(2.0*math.pi*i*hz/sps)
    return a

#加权叠加
def superpost(a,b,aWeight,bWeight):
    c=stdarray.create1D(len(a),0.0)
    for i in range(len(a)):
        c[i]=aWeight*a[i]+bWeight*b[i]
    return c

def note(pitch,duration):
    hz=440.0*(2.0**(pitch/12.0))
    lo=tone(hz/2,duration)
    hi=tone(2*hz,duration)
    harmonics=superpost(lo,hi,0.5,0.5)
    a=tone(hz,duration)
    return superpost(harmonics,a,0.5,0.5)

while not stdio.isEmpty():
    pitch=stdio.readInt()
    duration=stdio.readFloat()
    a=note(pitch,duration)
    stdaudio.playSamples(a)

stdaudio.wait()