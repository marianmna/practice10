try:
    with open('input.txt', 'r') as input_file:
        n = int(input_file.readline().strip())
        lines = input_file.readlines()

        if n == len(lines):
            result = "YES"
        else:
            result = "NO"

    with open('output.txt', 'w') as output_file:
        output_file.write(result)

except ValueError:
    print("ERROR: Первая строка должна содержать целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
