import os

if not os.path.exists('simple'):
    os.makedirs('simple')

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

output_path = os.path.join('simple', 'output.txt')
with open(output_path, 'w') as output_file:
    for i, line in enumerate(lines):
        if i % 2 == 1:
            output_file.write(line)
