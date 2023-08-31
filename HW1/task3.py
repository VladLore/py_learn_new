number = int(input("Введите число: "))
if number <= 0 or number > 10_000:
    print("Некорректное значение")
else:
    if number == 1 or number == 2:
        print("Число простое")
    else:
        is_prime = True
        for i in range(3, int(number**0.5)+1, 2):
            if number % i == 0:
                is_prime = False
            break
        if is_prime:
            print("Число составное")
        else:
            print("Число не является составным")