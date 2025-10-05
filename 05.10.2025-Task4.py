base = float(input("Основание треугольника: "))
height = float(input("Высота треугольника: "))

if base > 0 and height > 0:
    area = (base * height) / 2
    print(f"Площадь треугольника: {area}")
else:
    print("Ошибка! Основание и высота должны быть положительными числами.")