try:
    # Открываем файл input.txt для чтения
    with open('input.txt', 'r') as input_file:
        # Считываем первую строку с количеством строк N
        n = int(input_file.readline().strip())

        # Считаем количество строк в файле
        lines = input_file.readlines()

        # Проверяем, соответствует ли количество строк N фактическому количеству строк в файле
        if n == len(lines):
            result = "YES"
        else:
            result = "NO"

    # Записываем результат в файл output.txt
    with open('output.txt', 'w') as output_file:
        output_file.write(result)

except ValueError:
    print("ERROR: Первая строка должна содержать целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
