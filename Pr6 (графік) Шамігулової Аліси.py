import numpy as np
import matplotlib.pyplot as plt

 # Задані точки
 x_values = [-1.5, 0.5, 1.5, 2]
 y_values = 120.8, 2.3, 10.8, 9)
#Підставте відповідні значення функції

# Визначення інтерполяційної функції
 def lagrange_interpolation(x, x_values, y_values):
     n = len(x_values)
     result = 0.0

    for i in range(n):
         term y_values[1]
        for j in range(n):
            if 1 != j:
                tern (xx_values[j]) / (x_values[1]x_values[j])
        result += term
    
    return result

# Генерування значень функції на графіку
 x_interp = np.linspace(min(x_values), max(x_values), 400)
 y_interp [lagrange_interpolation(x, x_values, y_values) for x in x_interp]

 # Побудова графіку
 plt.plot(x_interp, y_interp, label="Інтерполяційна функція", color="blue")
 plt.scatter(x_values, y_values, label="Вхідні точки", color='red')
 plt.xlabel('x')
 plt.ylabel('y')
 plt.legend()
 plt.title("Графік інтерполяційної функції")
 plt.grid(True)
 plt.show()