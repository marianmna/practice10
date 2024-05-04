with open('input.txt', 'r') as file:
    data = file.read()

data_upper = data.upper()

with open('output.txt', 'w') as file:
    file.write(data_upper)
