try:
    with open('input.txt', 'r') as input_file:
        numbers = [int(num) for num in input_file.readline().split()]
        result = numbers[0] / numbers[1] + numbers[2]

    with open('output.txt', 'w') as output_file:
        output_file.write(str(result))

except ValueError:
    print("Ошибка: Неверный формат чисел в файле.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
