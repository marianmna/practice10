# Открываем файл input.txt для чтения и файл output.txt для записи
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Читаем строки из файла input.txt
    for line in input_file:
        # Проверяем, начинается ли строка с латинской буквы A (в верхнем или нижнем регистре)
        if line.strip().startswith('A') or line.strip().startswith('a'):
            # Если да, записываем эту строку в файл output.txt
            output_file.write(line)

print("Программа выполнена успешно. Проверьте файл output.txt.")
