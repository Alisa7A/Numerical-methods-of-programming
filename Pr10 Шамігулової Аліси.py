import numpy as np
import matplotlib.pyplot as plt
i_values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
xi_values = np.array([0.1 * i for i in i_values])
yi_values = np.sin(4 * xi_values)
table = np.vstack((i_values, xi_values, yi_values)).T
header = ["i", "xi", "f(xi)"]
print("{:<2} {:<5} {:<8}".format(*header))
for row in table:
    print("{:<2} {:<5} {:<8}".format(int(row[0]), row[1], round(row[2], 4)))
A_straight = np.vstack([xi_values, np.ones_like(xi_values)]).T
m_straight, c_straight = np.linalg.lstsq(A_straight, yi_values, rcond=None)[0]
A_parabola = np.vstack([xi_values**2, xi_values, np.ones_like(xi_values)]).T
a_parabola, b_parabola, c_parabola = np.linalg.lstsq(A_parabola, yi_values, rcond=None)[0]
x_range = np.linspace(0, 1, 100)
y_straight = m_straight * x_range + c_straight
y_parabola = a_parabola * x_range**2 + b_parabola * x_range + c_parabola
plt.scatter(xi_values, yi_values, label='Точки')
plt.plot(x_range, y_straight, label=f'Пряма: y = {m_straight:.4f}x + {c_straight:.4f}')
plt.plot(x_range, y_parabola, label=f'Парабола: y ={a_parabola:.4f}x^2 +  {b_parabola:.4f}x + {c_parabola:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()