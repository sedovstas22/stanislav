
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
    
if start > end:
        print("Ошибка! Начало диапазона не может быть больше конца")
else:
        print("\n" + "="*50)
        print(f"Анализ диапазона от {start} до {end}")
        print("="*50)
                
        print("\n1. Все числа диапазона:")
        all_numbers = list(range(start, end + 1))
        print(*all_numbers)
                
        print("\n2. Все числа диапазона в убывающем порядке:")
        descending_numbers = list(range(end, start - 1, -1))
        print(*descending_numbers)
                
        print("\n3. Все числа, кратные 7:")
        multiples_of_7 = [num for num in all_numbers if num % 7 == 0]
        if multiples_of_7:
            print(*multiples_of_7)
        else:
            print("В диапазоне нет чисел, кратных 7")
                
        print("\n4. Количество чисел, кратных 5:")
        count_multiples_of_5 = sum(1 for num in all_numbers if num % 5 == 0)
        print(f"Найдено чисел: {count_multiples_of_5}")
                
        multiples_of_5 = [num for num in all_numbers if num % 5 == 0]
        if multiples_of_5:
            print(f"Числа: {multiples_of_5}")
        else:
            print("В диапазоне нет чисел, кратных 5")
            
