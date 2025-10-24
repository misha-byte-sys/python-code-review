def ADD(x,y):
    return x+y

def subtract(a, b):
    return a - b

def multiply(a, b):
    c = a * b
    return c

def divide(a, b):
    return a / b

def main():
    print("Калькулятор")
    print("1: Сложение")
    print("2: Вычитание") 
    print("3: Умножение")
    print("4: Деление")
    
    r = 0
    choice = input("Выберите операцию (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        if choice == '1':
            result = ADD(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        if result > 100:
            print("Результат очень большой!")
        else:
            print(f"Результат: {result}")
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
