# Открываем файл input.txt для чтения и файл output.txt для записи
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    result = ""  # Переменная для хранения результата

    # Читаем строки из файла input.txt
    for line in input_file:
        # Получаем первый символ строки (если строка не пустая)
        if line.strip():  # Проверяем, что строка не пустая
            result += line[0]  # Добавляем первый символ к результату

    # Записываем полученный результат в файл output.txt
    output_file.write(result)

print("Программа выполнена успешно. Проверьте файл output.txt.")
