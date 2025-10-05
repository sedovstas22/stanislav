meters = float(input("Введите количество метров: "))
choice = int(input("Выберите: 1 для миль, 2 для дюймов, 3 для ярдов: "))

if choice == 1:
    result = meters / 1609.34 
    print("В милях: ", result)
elif choice == 2:
    result = meters / 0.0254 
    print("В дюймах: ", result)
elif choice == 3:
    result = meters / 0.9144  
    print("В ярдах: ", result)
else:
    print("Неверный выбор! Введите 1, 2 или 3.")