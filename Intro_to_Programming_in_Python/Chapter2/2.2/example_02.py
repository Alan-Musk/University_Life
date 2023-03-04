import sys
import stdio
import example_01

mu=float(sys.argv[1])
sigma=float(sys.argv[2])

for score in range(400,1600+1,100):
    percent=example_01.cdf(score,mu,sigma)
    stdio.writef('%4d  %.4f\n',score,percent)
