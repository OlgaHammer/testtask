def main(input_str: str):
    parts = input_str.split()
    if len(parts) != 3:
        raise ValueError("Неверный формат ввода. Используйте формат 'a + b'.")

    a, operator, b = parts

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("Числа должны быть целыми числами.")

    if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("Деление на ноль.")
        result = a // b  # Целочисленное деление
    else:
        raise ValueError("Неверный оператор. Используйте +, -, * или /.")

    return str(result)

while True:
    user_input = input("Введите выражение (например, 2 + 3) или 'exit' для выхода: ")
    if user_input.lower() == 'exit':
        break
    try:
        print(main(user_input))
    except ValueError as e:
        print(f"Произошла ошибка: {e}")
        break