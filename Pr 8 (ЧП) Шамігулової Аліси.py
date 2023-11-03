import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
x = np.array([0.4, 0.6, 0.9, 1.4, 2])
y = np.array([2.45, 1.63, 0.95, 0.73, 1.95])

n = len(x) - 1
h = np.diff(x)
a = y
b = np.zeros(n)
d = np.zeros(n)
c = np.zeros(n)

alpha = np.zeros(n)
for i in range(1, n):
    alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

l = np.ones(n)
mu = np.zeros(n)
z = np.zeros(n)

for i in range(1, n):
    l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
    mu[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

c[n - 1] = (alpha[n - 1] - h[n - 2] * z[n - 2]) / (2 * (h[n - 2] + mu[n - 1]))
b[n - 1] = (a[n] - a[n - 1]) / h[n - 1] - h[n - 1] * (2 * c[n - 1] + c[n - 2]) / 3
d[n - 1] = (c[n - 1] - c[n - 2]) / (3 * h[n - 1])

for j in range(n - 2, -1, -1):
    c[j] = z[j] - mu[j] * c[j + 1]
    b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
    d[j] = (c[j + 1] - c[j]) / (3 * h[j])

for i in range(n):
    print(f"Відрізок {i + 1}:")
    print(f"S_{i}(x) = {a[i]} + {b[i].round(4)}(x - {x[i]}) + {c[i].round(4)}(x - {x[i]})^2 + {d[i].round(4)}(x - {x[i]})^3, x належить [{x[i]}, {x[i + 1]}]")

cs = CubicSpline(x, y)

x_new = np.linspace(np.min(x), np.max(x), 100)
y_new = cs(x_new)
print("Значення сплайна:")
for i in range(len(x_new)):
    print(f"x = {x_new[i]:.2f}, y = {y_new[i]:.3f}")

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Точки')
plt.plot(x_new, y_new, label='Кубічний сплайн')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кубічний сплайн')
plt.legend()
plt.grid(True)
plt.show()

derivatives_at_specific_points = cs(x=np.array([0.7, 1.5, 2.0]), nu=1)
print("Перші похідні у вказаних точках:")
for i in range(len(derivatives_at_specific_points)):
    print(f"x = {x[i]:.2f}, Похідна = {derivatives_at_specific_points[i]:.3f}")