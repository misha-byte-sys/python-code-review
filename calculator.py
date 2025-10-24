def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
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
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите число")
            return
        
        if choice == '1':
            print(f"Результат: {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Результат: {divide(num1, num2)}")
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
