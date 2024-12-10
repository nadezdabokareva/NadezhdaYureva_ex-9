def fibonacci_sum(n):
    # Первые два числа ряда Фибоначчи
    a, b = 0, 1
    total_sum = 0

    for i in range(n):
        total_sum += a
        a, b = b, a + b  # Обновляем значения чисел Фибоначчи

    return total_sum


# Ввод пользователя
try:
    n = int(input("Введите количество чисел из ряда Фибоначчи: "))
    if n < 0:
        print("Число должно быть положительным!")
    else:
        result = fibonacci_sum(n)
        print(f"Сумма первых {n} чисел ряда Фибоначчи: {result}")
except ValueError:
    print("Пожалуйста, введите целое число.")