# напиши код для выполнения заданий здесь
def ex_one():
    count = 0
    with open('my_file.txt', 'r') as file:
        for string in file:
            items = string.split(' ')
            for item in items:
                if int(item) == 1:
                    count += 1
    print('Количество "1" в файле =', count)

# ex_one()              26

def ex_two():
    with open('my_file.txt', 'r') as file:
        lines = file.readlines()
        second_line = lines[13].split(' ')
        print(second_line[7])

# ex_two()              1

def ex_three():
    summ = 0
    with open('my_file.txt', 'r') as file:
        for string in file:
            items = string.split(' ')
            for item in items:
                summ += int(item)
    print('Сумма всех чисел из файла =', summ)

ex_three()