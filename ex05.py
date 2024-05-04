try:
    # Открываем файл input.txt для чтения
    with open('input.txt', 'r') as input_file:
        # Считываем три целых числа из файла input.txt
        numbers = [int(num) for num in input_file.readline().split()]

        # Делим первое число на второе и прибавляем третье число
        result = numbers[0] / numbers[1] + numbers[2]

    # Записываем результат в файл output.txt
    with open('output.txt', 'w') as output_file:
        output_file.write(str(result))

except ValueError:
    print("Ошибка: Неверный формат чисел в файле.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
