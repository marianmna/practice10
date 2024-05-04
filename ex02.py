with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        if line.strip().startswith('A') or line.strip().startswith('a'):
            output_file.write(line)

print("Программа выполнена успешно. Проверьте файл output.txt.")
