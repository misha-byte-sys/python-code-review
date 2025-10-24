def add(a, b):  # Исправлено: PEP 8
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b  # Исправлено: убрана избыточная переменная

def divide(a, b):
    if b == 0:  # Исправлено: добавлена проверка безопасности
        return "Ошибка: деление на ноль"
    return a / b

def main():
    print("Калькулятор")
    print("1: Сложение")
    print("2: Вычитание")
    print("3: Умножение") 
    print("4: Деление")
    
    choice = input("Выберите операцию (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        try:  # Исправлено: добавлена обработка ошибок ввода
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите корректное число")
            return
        
        if choice == '1':
            result = add(num1, num2)  # Исправлено: правильное имя функции
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        if result > 100:  # Можно вынести MAX_RESULT = 100
            print(f"Результат очень большой: {result}")  # Исправлено: форматирование
        else:
            print(f"Результат: {result}")
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
