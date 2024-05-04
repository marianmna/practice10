with open('input.txt', 'r') as file:
    steps_data = file.readlines()
monthly_steps = [0] * 12

for steps in steps_data:
    steps_per_day = int(steps)
    month = (steps_data.index(steps) // 31)
    monthly_steps[month] += steps_per_day

average_steps_per_month = [total_steps // 31 for total_steps in monthly_steps]

with open('output.txt', 'w') as file:
    for steps in average_steps_per_month:
        file.write(str(steps) + '\n')
