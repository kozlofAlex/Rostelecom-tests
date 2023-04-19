# Тестирование интерфейса авторизации [Ростелеком Информационные Технологии](https://b2c.passport.rt.ru)

- [Требования](Требования_SSO_для_тестирования_last.doc)
- [Тест-кейсы](https://docs.google.com/spreadsheets/d/1duoCbv6G1kaRiQWd_4oMSMEwf3PxO2jHrazATA9jh2g/edit?usp=sharing) 
- [Автоматизированные тест-кейсы](tests/auth_rostelecom_tests.py)

Инструкция для запуска тест-кейсов: <br>
1. Скопировать git репозиторий, выполнив команду: <br> 
``` git clone https://github.com/kozlofAlex/Rostelecom-tests.git  ```
2. Установить библиотеки из файла requirements <br>
``` pip3 install -r requirements```
3. Запустить тесты через Терминал, выполнив команду: <br> 
``` python -m pytest -v --driver Chrome --driver-path \chromedriver.exe auth_rostelecom_tests.py ```