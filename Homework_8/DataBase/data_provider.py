def input_name ():
    new_name = input ('Введите имя: ')
    new_name = new_name.title()
    new_surname = input ('Введите фамилию: ')
    new_surname = new_surname.title()
    new_patronymic = input ('Введите отчество: ')
    new_patronymic = new_patronymic.title()
    list_name = (new_name, new_surname, new_patronymic)
    return list_name

def input_number ():
    new_number = input ('Введите номер телефона: ')
    return new_number

def input_job_info ():
    new_job = input ('Введите должность: ')
    new_salary = input ('Введите зароботную плату: ')
    job_info = [new_job, new_salary]
    return job_info

def input_comment ():
    new_com = input ('Введите комментарий: ')
    return new_com