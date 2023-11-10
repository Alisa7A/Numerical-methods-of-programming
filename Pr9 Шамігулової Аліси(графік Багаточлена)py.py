import numpy as np
inport matpotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial
import sympy as sp

def f(x):
    return np.sin(4 * x)
x0 = 0
degree = 3
x = np.linspace(-2, 2, 1000)
f_vals = f(x)
taylor_poly = approximate_taylor_polynomial(f, x0, degree, scale=1.0)
taylor_vals = taylor_poly(x)
x_sym = sp.symbols('x')
f_sym = sp.sin(4 * x_sym)
f_prime_sym = f_sym.diff(x_sym)
f_double_prime_sym = f_prime_sym.diff(x_sym)
f_triple_prime_sym = f_double_prime_sym.diff(x_sym)
print("Функция f(x):", f_sym)
print("Первая производная f'(x):", f_prime_sym)
print("Вторая производная f''(x):", f_double_prime_sym)
print("Третья производная f'''(x):", f_triple_prime_sym)
x0_val = 0
f_x0 = f(x0_val)
taylor_x0 = taylor_poly(x0_val)
remainder = f_x0 - taylor_x0
print("Значение функции в х=0:", f_x0)
print("Значение полинома Тейлора в x=0:", taylor_x0)
print("Оценка погрешности в x=0:", remainder)
plt.figure(fisize=(10,6))
plt.plot(x, f_vals, label=f"Taylor Polynomial (Degree {degree})", color='red', linestyle='--')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции и аппроксимации полиномом Тейлора")
plt.grid()
plt.show()