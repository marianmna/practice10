with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

current_date = lines[0].strip()

occupied_cells = int(lines[1])

result_cells = []

for line in lines[2:]:
    cell_number, date = line.strip().split()
    day, month = map(int, date.split('.'))
    diff_days = (int(current_date[:2]) - int(day)) + (30 * (int(current_date[3:]) - int(month))

    if diff_days > 3:
        result_cells.append(cell_number)

    with open('output.txt', 'w') as output_file:
        for
    cell in result_cells: \
        output_file.write(cell + '\n')

