# Открываем файл input.txt для чтения
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Открываем файл input.txt для записи (перезапись)
with open('input.txt', 'w') as file:
    for line in lines:
        if '100' not in line:  # Проверяем, не содержит ли строка число 100
            file.write(line)
