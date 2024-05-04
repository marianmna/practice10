# Открываем файл input.txt для чтения
with open('input.txt', 'r') as file:
    data = file.read()

# Преобразуем данные к верхнему регистру
data_upper = data.upper()

# Открываем файл output.txt для записи
with open('output.txt', 'w') as file:
    file.write(data_upper)
