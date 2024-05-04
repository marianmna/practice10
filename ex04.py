# Открываем файл input.txt для чтения и файл output.txt для записи
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Читаем строки из файла input.txt
    for line in input_file:
        # Проверяем, содержит ли строка более 20 символов
        if len(line) > 20:
            # Записываем строку в файл output.txt
            output_file.write(line)

print("Программа выполнена успешно. Проверьте файл output.txt.")
