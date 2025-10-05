num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

choice = int(input("Выберите: 1 для суммы, 2 для произведения: "))

if choice == 1:
    result = num1 + num2 + num3
    print("Сумма:", result)
elif choice == 2:
    result = num1 * num2 * num3
    print("Произведение:", result)
else:
    print("Неверный выбор! Введите 1 или 2.")