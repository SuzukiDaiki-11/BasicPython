from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

def trapezoidal(f, a, b, N):
    h = (b - a) / N
    S = 0

    for k in range(1, N+1):
        S += (h / 2) * (sin(a + (k-1) * h) + sin(a + k * h))

    return S

result = trapezoidal(math.sin, 0, math.pi/2, 100)
print(result)

# 区間 [0, π/2] のsin関数の積分を台形積分で近似
