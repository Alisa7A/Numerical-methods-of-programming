def lagrange_interpolation(x, x_values, y_values):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range (n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    
    return result

#Ваші вхідні дані
x_values = [-3, -2, 1, 3]
y_values = [-4, 19, -8, 14]

#Ваші точки, в яких ви хочете обчислити значення функції
points_to_evaluate = [-1.5, 0.5, 1.5, 2]

#Обчислюємо значення функції в заданих точках
for x in points_to_evaluate:
    result = lagrange_interpolation(x, x_values, y_values)
    print(f"f({x}) = {result:.3f}")