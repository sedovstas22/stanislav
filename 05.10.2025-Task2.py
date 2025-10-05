num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

choice = int(input("Выберите: 1 для максимума, 2 для минимума, 3 для среднего: "))

if choice == 1:
    result = max(num1, num2, num3)
    print("Максимум:", result)
elif choice == 2:
    result = min(num1, num2, num3)
    print("Минимум:", result)
elif choice == 3:
    result = (num1 + num2 + num3) / 3
    print("Среднее:", result)
else:
    print("Неверный выбор! Введите 1, 2 или 3.")