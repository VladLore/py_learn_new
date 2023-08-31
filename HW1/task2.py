a = float(input("Введите сторону a: ")) 
b = float(input("Введите сторону b: ")) 
c = float(input("Введите сторону c: ")) 
 
if a >= b+c or b >= a+c or c >= a+b: 
    print("Треугольника с такими сторонами не существует") 
else: 
    print("Треугольник существует")