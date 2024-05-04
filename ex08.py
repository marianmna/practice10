# Считываем данные из файла input.txt
with open('input.txt', 'r') as file:
    steps_data = file.readlines()

# Создаем список для хранения суммарного количества шагов для каждого месяца
monthly_steps = [0] * 12

# Вычисляем суммарное количество шагов для каждого месяца
for steps in steps_data:
    steps_per_day = int(steps)
    month = (steps_data.index(steps) // 31)  # Определяем месяц по индексу дня
    monthly_steps[month] += steps_per_day

# Вычисляем среднесуточное количество шагов для каждого месяца
average_steps_per_month = [total_steps // 31 for total_steps in monthly_steps]

# Записываем результат в файл output.txt
with open('output.txt', 'w') as file:
    for steps in average_steps_per_month:
        file.write(str(steps) + '\n')
