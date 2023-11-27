# Довільні точки х, для яких ми хочемо побудувати графік
x_interp np.array([1.342, 1.346, 1.361, 1.381, 1.386, 1.394])
# Функція для обчислення інтерполяційного багаточлена Ньютона
def newton_interpolation(x, x_data, y_data):
    n = len(x_data)
    f = y_data.copy()
    for i in range(1, n):
        f[0:n-1] = ((x-x_data[i:]) * f[0:n-i] - (x - x_data[:n-i]) * f[1:n-i+1]) / (x_data[0:n-i] - x_data[i:])
    return f[0]
# Знаходимо значення функції в точках x_interp
y_interp = [newton_interpolation(x, x_data, y_data) for x in x_interp]
# Побудова графіка
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Дані точки", color='red', marker='o')
plt.plot(x_interp, y_interp, label='Інтерполяція", color='blue', linestyle-'--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Графік інтерполяційної функції")
plt.grid(True)
plt.show()