# Тестирование интерфейса авторизации [Ростелеком Информационные Технологии](https://b2c.passport.rt.ru)

- [Требования по проекту](https://lms.skillfactory.ru/assets/courseware/v1/f78e146f0eb3ace247a28b07e66467de/asset-v1:SkillFactory+INTQAP+2022+type@asset+block/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_SSO_%D0%B4%D0%BB%D1%8F_%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_last.doc)
- [Тест-кейсы](https://docs.google.com/spreadsheets/d/1duoCbv6G1kaRiQWd_4oMSMEwf3PxO2jHrazATA9jh2g/edit?usp=sharing)
- [Баг репорты](https://docs.google.com/spreadsheets/d/1duoCbv6G1kaRiQWd_4oMSMEwf3PxO2jHrazATA9jh2g/edit#gid=1337123936)
- [Автоматизированные тест-кейсы](tests/auth_rostelecom_tests.py)

<b>Требования:</b>

- Python 3.8 (и выше)
- IDE Python (PyCharm, Atom, Microsoft Visual Studio или др.)
- GIT 

<b>Инструкция для запуска тест-кейсов: </b><br>
1. Скопировать git репозиторий, выполнив команду: <br> 
``` git clone https://github.com/kozlofAlex/Rostelecom-tests.git  ```
2. Установить библиотеки из файла requirements <br>
``` pip3 install -r requirements.txt```
3. Запустить тесты через Терминал, выполнив команду: <br> 
``` python -m pytest -v --driver Chrome --driver-path \chromedriver.exe tests\auth_rostelecom_tests.py ```