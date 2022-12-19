# import sys
# import math
# import stdio

# num=int(sys.argv[1])


# stdio.writeln(math.cos(num)*math.cos(num)+math.sin(num)*math.sin(num))

import sys 
import stdio
import math

theta=float(sys.argv[1])
theta_in_rad=math.radians(theta)

val_of_sin=math.sin(theta_in_rad)
val_of_cos=math.cos(theta_in_rad)

result=(val_of_sin**2)+(val_of_cos**2)
stdio.writeln(str(result))