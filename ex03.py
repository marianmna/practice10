with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    result = ""

    for line in input_file:
        if line.strip():
            result += line[0]

    output_file.write(result)

print("Программа выполнена успешно. Проверьте файл output.txt.")
