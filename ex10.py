# Чтение данных из файла input.txt
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

# Получение текущей даты из первой строки исходного файла
current_date = lines[0].strip()

# Получение количества занятых ячеек из второй строки исходного файла
occupied_cells = int(lines[1])

# Создание списка для хранения номеров ячеек, в которых багаж хранится более 3 дней
result_cells = []

# Проверка каждой строки с информацией о ячейке
for line in lines[2:]:
    cell_number, date = line.strip().split()
    day, month = map(int, date.split('.'))

    # Расчет разницы в днях между текущей датой и датой сдачи багажа
    diff_days = (int(current_date[:2]) - int(day)) + (30 * (int(current_date[3:]) - int(month))

    if diff_days > 3:
        result_cells.append(cell_number)

    # Запись результатов в файл output.txt
    with open('output.txt', 'w') as output_file:
        for
    cell in result_cells: \
        output_file.write(cell + '\n')

