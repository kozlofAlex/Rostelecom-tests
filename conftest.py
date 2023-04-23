driverPathChrome = 'chromedriver.exe'
baseUrl = 'https://b2c.passport.rt.ru'

# Корректные значения
registerFormKeysFirstName_correct = ['Ян', 'Анна-Мария', 'аааааааааааааааааааааааааааааа']
registerFormKeysLastName_correct = ['Ли', 'Салтыков-Щедрин', 'аааааааааааааааааааааааааааааа']
registerFormKeysAddress_correct = ['+72222222222', '+375222222222', 'test@mail.ru']
registerFormPassword_correct = ['QWERTYq1']
registerKeysDict_correct = {
    'firstName': registerFormKeysFirstName_correct,
    'lastName': registerFormKeysLastName_correct
}

# Некорректные значения
registerFormKeysFirstName_not_correct = ['A', 'Ab', '!!!!!', 'ааааааааааааааааааааааааааааааа']
registerFormKeysLastName_not_correct = ['A', 'Ab', '!!!!!', 'ааааааааааааааааааааааааааааааа']
registerFormKeysAddress_not_correct = ['A', '!@#$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', '9099900015', 'test@mail.ru']
registerFormPassword_not_correct = ['а', 'аааааааа', 'abcdefgh', 'abcdefgh1']
registerKeysDict_not_correct = {
    'firstName': registerFormKeysFirstName_not_correct,
    'lastName': registerFormKeysLastName_not_correct
}

# Ошибки
registerErrorsName = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
registerErrorsAddress = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
registerErrorsPasswordConfirm = 'Пароли не совпадают'
regErPass = 'Длина пароля должна быть не менее 8 символов'
