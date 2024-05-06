from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------


# 区間 [0, π/2] のsin関数の積分を台形積分で近似

import math
from math import pi

def trapezoidal_integration(f, a=0, b=1, n=100):
    h = (b - a) / n
    S = 0
    for i in range(1, n):
        S += (h / 2) * (f(a + i * h) + f(a + (i + 1)* h))
    return S


# (1) 
def sinX(x):
    return math.sin(x)

integral_1 = trapezoidal_integration(sinX, 0, math.pi/2, 50)
print("(1)の結果:", integral_1)

# (2) 
def function_2(x):
    return 4 / (1 + x**2)

integral_2 = trapezoidal_integration(function_2, 0, 1, 100)
print("(2)の結果:", integral_2)

# (3) 
def function_3(x):
    if x >= 0:
        return math.sqrt(math.pi) * math.exp(-x**2)
    else:
        return 0
    

integral_3 = trapezoidal_integration(function_3, -100, 100, 1000)
print("(3)の結果:", integral_3)
