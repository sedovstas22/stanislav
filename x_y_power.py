x = int(input("Введите число x: "))
y = int(input("Введите степень y: "))
result = x ** y    
if result == x ** y:
    print(f"{x} в степени {y} = {result}")
else:
    print('Введите целые числа')