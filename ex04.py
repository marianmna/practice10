with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:

    for line in input_file:
        if len(line) > 20:
            output_file.write(line)

print("Программа выполнена успешно. Проверьте файл output.txt.")
