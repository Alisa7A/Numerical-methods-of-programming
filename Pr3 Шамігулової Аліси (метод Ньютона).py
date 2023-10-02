def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 5
    
def df(x):
    return 4*x**3 + 6*x**2 + 4*x + 6
    
def newton_method (f,df,x0,epsilon):
    x=x0
    while abs(f(x))>epsilon:
        x=x-f(x)/df(x)
    return x

x0_1=-2.5
x0_2=0.5
epsilon=0.0001

root1=newton_method(f, df, x0_1, epsilon)
root2=newton_method(f, df, x0_2, epsilon)

print(f"Корінь на відрізку [-3,-2]: {root1}")
print(f"Корінь на відрізку [0,1]:{root2}")
