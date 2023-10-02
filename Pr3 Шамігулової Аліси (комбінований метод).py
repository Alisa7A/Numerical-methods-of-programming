def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 5
def df(x):
    return 4*x**3 + 6*x**2 + 4*x + 6

def combined_method(f, a, b, epsilon):
    if f(a) * f(b) > 0:
        print ("На вказаному відрізку немає коренів.")
        return None
     
    while (b-a)/2>epsilon:
        c= (a+b)/2
        if f(c)==0:
            return c
        elif f(a) * f(c) < 0:
            b=c
        else:
            a=c
        
    return (a+b)/2
a1,b1=-3, -2
a2,b2=0, 1
epsilon=0.0001
root1=combined_method(f, a1, b1, epsilon)
root2=combined_method(f, a2, b2, epsilon)
print(f"Корінь на відрізку [-3,-2]: {root1}")
print(f"Корінь на відрізку [0,1]:{root2}")