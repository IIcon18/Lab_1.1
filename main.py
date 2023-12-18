print("Введите коэфициенты для уравнения ax^2+bx+c=0")
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))
D = 0

if a == 0:
    print("x =", c / b)
else:
    D = b ** 2 - 4 * a * c
    print(D)
    if D < 0:
        print('Корней нет!')

    elif D == 0:
        print('x =', -b / (2 * a))

    elif D > 0:
        print('x1 =', (-b - D ** 0.5) / (2 * a))
        print('x2 =', (-b + D ** 0.5) / (2 * a))