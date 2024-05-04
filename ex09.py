import os

# Проверяем наличие каталога simple и создаем его, если он не существует
if not os.path.exists('simple'):
    os.makedirs('simple')

# Считываем данные из файла input.txt
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

# Отбираем четные строки и записываем их в файл output.txt в каталоге simple
output_path = os.path.join('simple', 'output.txt')
with open(output_path, 'w') as output_file:
    for i, line in enumerate(lines):
        if i % 2 == 1:  # Проверяем, является ли номер строки четным
            output_file.write(line)
