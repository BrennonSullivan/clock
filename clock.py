def clockadd(P1,P2):
  x1,y1 = P1
  x2,y2 = P2
  x3 = x1*y2+y1*x2
  y3 = y1*y2-x1*x2
  return x3,y3

# example:
P1 = (1000,2)
P2 = (1000^2,2^2)

print clockadd(P1,P2)
# output: (0.936, 0.3519999999999999)
print clockadd(P2,P1)
# output: (0.936, 0.3519999999999999)
# perfect real output would have been (0.936, 0.352)

import math

def oclock(time):
  radians = time * math.pi / 6
  return math.sin(radians),math.cos(radians)

print clockadd(oclock(4),oclock(1))
# output: (0.5000000000000002, -0.8660254037844385)
print oclock(5)
# output: (0.49999999999999994, -0.8660254037844387)
# perfect real output would have matched
P3 = clockadd(P2,P1)
print P3
P6 = clockadd(P3,P3)
print P6