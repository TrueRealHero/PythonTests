import csv
import os.path

coma = print('*' * 20)

if os.path.exists('csv_data_file.csv'):
    pass
else:
    with open('csv_data_file.csv', 'w', newline='') as data_file:
        fieldnames = ['First Name', 'Last Name', 'Telefon Number']
        data_writer = csv.DictWriter(data_file, fieldnames=fieldnames, delimiter='\t')
        data_writer.writeheader()

def dictionary():
    coma
    print('''Выберите опцию!
    1 - Добавить нового пользователя
    2 - Поиск по имени или номеру телефона
    3 - Удалить пользователя''')
    try:
        option_select = int(input())
    except ValueError:
        print('Пожалуйста введите номер опций!')
        dictionary()
    if option_select not in range (1,4):
        print("Вы выбрали несуществущюю опцию! Попробуйте снова.")
        dictionary()
    elif option_select == 1:
        add_new_user()
    elif option_select == 2:
        search_user()
    elif option_select == 3:
        delete_user()

def add_new_user():
    print('Введите пожалуйста данные в соответствующие поля:')
    first_name = str(input('Ввведите Ваше имя: '))
    last_name = str(input('Ввведите Вашу фамилию: '))
    tel_number = int(input('Введите Ваш номер телефона: '))
    with open('csv_data_file.csv', 'a', newline='') as data_file:
        fieldnames = ['First Name', 'Last Name', 'Telefon Number']
        data_writer = csv.DictWriter(data_file, fieldnames=fieldnames, delimiter='\t')
        data_writer.writerow({'First Name':first_name,
                            'Last Name':last_name,
                            'Telefon Number':tel_number})

def search_user():
    print('Введите Имя \ Фамилию или номер телефона для поиска: ')
    search_word = input()
    with open('csv_data_file.csv', 'r') as data_file:
        data_reader = csv.DictReader(data_file, delimiter = '\t')
        for line in data_reader:
            if search_word in line.values():
                print(line)

def delete_user():
    print('Здесь вы можете удалить пользователя по имени или номеру телефона: ')
    delete_word = input()
    buffer=list(dict())
    with open('csv_data_file.csv', 'r', newline='') as data_file:
        data_reader = csv.DictReader(data_file, delimiter = '\t')
        for line in data_reader:
            if delete_word not in line.values():
                buffer.append(line)
    with open('csv_data_file.csv', 'w', newline='') as data_file:
        with open('csv_data_file.csv', 'a', newline='') as data_file:
                fieldnames = ['First Name', 'Last Name', 'Telefon Number']
                data_appender = csv.DictWriter(data_file, fieldnames=fieldnames, delimiter='\t')
                data_appender.writeheader()
                for line in buffer:
                    data_appender.writerow(line)
          

              

dictionary()