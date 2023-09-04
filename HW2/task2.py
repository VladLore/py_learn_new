def sum_and_product(a, b):
    sum_ = a + b
    product = a * b
    return sum_, product


a = input("Введите числитель дроби: ")
b = input("Введите знаменатель дроби: ")
sum_, product = sum_and_product(eval(a), eval(b))
print("Сумма дробей:", sum_)
print("Произведение дробей:", product)
