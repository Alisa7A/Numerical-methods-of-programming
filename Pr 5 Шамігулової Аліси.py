import math
x0 = 1.0
y0 = 1.0
epsilon = 0.001 

def func_x(y):
    return math.sin(y + 1) + 0.8

def func_y(x):
    return 1.3 - math.sin(x - 1)

def check_accuracy(x_new, y_new, x_old, y_old, epsilon):
    return abs(x_new - x_old) < epsilon and abs(y_new - y_old) < epsilon
while True:
    x_new = func_x(y0)
    y_new = func_y(x0)
    
    if check_accuracy(x_new, y_new, x0, y0, epsilon):
        break
    
    x0 = x_new
    y0 = y_new
print("Розв'язок:")
print("x =", x_new)
print("y =", y_new)
