from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
def trapezoidal_integration(func, a, b, n):
    h = (b - a) / n
    integral_result = (func(a) + func(b)) / 2

    for k in range(1, n):
        x_k_minus_1 = a + (k - 1) * h
        x_k = a + k * h
        integral_result += func(x_k_minus_1) + func(x_k)

    integral_result *= h / 2

    return integral_result

# 区間 [0, π/2] のsin関数の積分を台形積分で近似
a_value = 0
b_value = (3.14 / 2)  
num_trapezoids = 100

result = trapezoidal_integration(sin, a_value, b_value, num_trapezoids)
