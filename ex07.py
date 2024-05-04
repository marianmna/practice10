with open('input.txt', 'r') as file:
    lines = file.readlines()

with open('input.txt', 'w') as file:
    for line in lines:
        if '100' not in line:
            file.write(line)
