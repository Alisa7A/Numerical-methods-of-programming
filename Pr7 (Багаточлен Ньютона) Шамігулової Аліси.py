import numpy as np

 # Задана таблиця значень
 x_values = [1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390]
 y_values = [4.2556, 4.3532, 4.4552, 4.5618, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706]

 # Функція для інтерполяції багаточленом Ньютона
 def interpolate_newton(x, x_values, y_values):
     n = len(x_values)
     result = 0
    for i in range(n):
         term = y_values[i]
        for j in range(n):
            if j != i:
                 term *= (x-x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# Виводимо значення f(х) для декількох довільних точок х
x_points [1.361, 1.394, 1.346, 1.381, 1.342, 1.386]

 for x in x_points:
     y = interpolate_newton(x, x_values, y_values)
     print(f"f({x}) = {y}")