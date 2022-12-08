def get_info ():
    list_info = []
    new_surname = input ('Введите фамилию: ')
    new_surname = new_surname.title()
    list_info.append(new_surname)
    new_name = input ('Введите имя: ')
    new_name = new_name.title()
    list_info.append(new_name)
    new_patronymic = input ('Введите отчество: ')
    new_patronymic = new_patronymic.title()
    list_info.append(new_patronymic)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    list_info.append(phone_number)
    description = input('Введите описание: ')
    list_info.append(description)
    return list_info