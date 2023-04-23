from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import conftest


def get_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=conftest.driverPathChrome, chrome_options=options)
    driver.get(conftest.baseUrl)
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    assert wait.until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="card-container__title"]'))).text == 'Авторизация'
    return driver, wait


# TK-1: Переход на форму "Зарегистрироваться"
def test_redirect_to_registration():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'
    driver.quit()


# TK-2: Регистрация по номеру мобильного телефона
def test_registration_phone():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('Александр').perform()  # указываем имя
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('Козлов').perform()  # указываем фамилию
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('+375123456789').perform()  # вводим номер телефона
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('QWERTYqwerty1').perform()  # вводим корректный пароль
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('QWERTYqwerty1').perform()  # повторяем введенный пароль
    driver.find_element(By.NAME, 'register').click()
    confirmPage = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Подтверждение телефона')]"))).text
    assert confirmPage == 'Подтверждение телефона'
    driver.quit()


# TK-3: Регистрация по email
def test_registration_email():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('Александр').perform()  # указываем имя
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('Козлов').perform()  # указываем фамилию
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('test_rostelecom@mail.ru').perform()  # вводим email
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('QWERTYqwerty1').perform()  # вводим корректный пароль
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('QWERTYqwerty1').perform()  # повторяем введенный пароль
    driver.find_element(By.NAME, 'register').click()
    confirmPage = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Подтверждение email')]"))).text
    assert confirmPage == 'Подтверждение email'
    driver.quit()


# TK-4: Проверка полей Имя и Фамилия страницы Регистрация на корректный ввод данных
def test_register_firstName_and_lastName_correct():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    firstNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
    lastNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'lastName')))
    elementsDictionary = {
        'firstName': firstNameInput,
        'lastName': lastNameInput
    }

    for key in conftest.registerKeysDict_correct:
        values = conftest.registerKeysDict_correct[key]
        actionChain.click(elementsDictionary[key]).perform()

        for j in range(len(values)):
            actionChain.send_keys(values[j]).perform()
            driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

            if j < len(values) - 1:
                if j >= 1:
                    pass
                actionChain.double_click(elementsDictionary[key]).click_and_hold().send_keys(Keys.DELETE).perform()
    driver.quit()


# TK-5: Проверка полей Имя и Фамилия страницы Регистрация на некорректный ввод данных
def test_register_firstName_and_lastName_not_correct():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    firstNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
    lastNameInput = wait.until(EC.presence_of_element_located((By.NAME, 'lastName')))
    elementsDictionary = {
        'firstName': firstNameInput,
        'lastName': lastNameInput
    }

    for key in conftest.registerKeysDict_not_correct:
        values = conftest.registerKeysDict_not_correct[key]
        actionChain.click(elementsDictionary[key]).perform()

        for j in range(len(values)):
            actionChain.send_keys(values[j]).perform()
            driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

            if j < len(values) - 1:
                if j >= 1:
                    pass
                else:
                    error = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text
                assert error == conftest.registerErrorsName
                actionChain.double_click(elementsDictionary[key]).click_and_hold().send_keys(Keys.DELETE).perform()
    driver.quit()


# TK-6: Проверка поля Email или Мобильный телефон страницы Регистрация на корректный ввод данных
def test_register_email_and_phone_correct():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    addressNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address')))
    values = conftest.registerFormKeysAddress_correct
    actionChain.click(addressNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            actionChain.double_click(addressNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
    driver.quit()


# TK-7: Проверка поля Email или Мобильный телефон страницы Регистрация на некорректный ввод данных
def test_register_password():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    passNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password')))
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,
         'section#page-right > div > div > div > form > div:nth-of-type(4) > '
         'div > div > div:nth-of-type(2) > svg'))).click()  # для наглядности отображаем пароль
    values = conftest.registerFormPassword_not_correct
    actionChain.click(passNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text

            actionChain.double_click(passNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
            assert error == conftest.regErPass
    driver.quit()


# TK-8: Проверка поля Пароль страницы Регистрация на корректный ввод данных
def test_register_password_correct():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    passNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password')))
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,
         'section#page-right > div > div > div > form > div:nth-of-type(4) > '
         'div > div > div:nth-of-type(2) > svg'))).click()  # для наглядности отображаем пароль
    values = conftest.registerFormPassword_correct
    actionChain.click(passNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
    driver.quit()


# TK-9: Проверка поля Пароль страницы Регистрация на некорректный ввод данных
def test_register_password_not_correct():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'
    passNameInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password')))
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,
         'section#page-right > div > div > div > form > div:nth-of-type(4) > '
         'div > div > div:nth-of-type(2) > svg'))).click()  # для наглядности отображаем пароль
    values = conftest.registerFormPassword_not_correct
    actionChain.click(passNameInput).perform()

    for j in range(len(values)):
        actionChain.send_keys(values[j]).perform()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личные данные')]").click()

        if j < len(values) - 1:
            if j >= 1:
                pass
            else:
                error = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error'))).text
            actionChain.double_click(passNameInput).click_and_hold().send_keys(Keys.DELETE).perform()
            assert error == conftest.regErPass
    driver.quit()


# TK-10: Проверка поля Подтверждение пароля на странице Регистрации
def test_register_passwordConfirm_correct():
    driver, wait = get_driver()
    actionChain = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
    assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-container__title'))).text == 'Регистрация'

    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).click()
    actionChain.send_keys('Александр').perform()
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).click()
    actionChain.send_keys('Козлов').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#address'))).click()
    actionChain.send_keys('+375123456789').perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > '
                                               'div > div > div:nth-of-type(2) > svg'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password'))).click()
    actionChain.send_keys('QWERTYq1').perform()  # вводим пароль
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               'section#page-right > div > div > div > form > div:nth-of-type(4) > '
                                               'div:nth-of-type(2) > div > div:nth-of-type(2) > svg > path'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#password-confirm'))).click()
    actionChain.send_keys('QWERTYq2').perform()  # вводим пароль, отличный от первого
    driver.find_element(By.NAME, 'register').click()
    error = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Пароли не совпадают')]"))).text
    assert error == 'Пароли не совпадают'
    driver.quit()


# TK-11: Переход на форму "Восстановление пароля"
def test_click_forgotPassword():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='forgot_password']"))).click()
    time.sleep(2)
    assert wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]"))).text == 'Восстановление пароля'
    driver.quit()


# TK-12: Авторизация пользователя с помощью учетной записи VK
def test_auth_vk():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_vk'))).click()
    assert driver.current_url.__contains__('oauth.vk.com')
    driver.quit()


# TK-13: Авторизация пользователя с помощью учетной записи  OK
def test_auth_ok():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_ok'))).click()
    assert driver.current_url.__contains__('connect.ok.ru')
    driver.quit()


# TK-14: Авторизация пользователя с помощью учетной записи  Mail.ru
def test_auth_mail():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_mail'))).click()
    assert driver.current_url.__contains__('connect.mail.ru')
    driver.quit()


# TK-15: Авторизация пользователя с помощью учетной записи  Google
def test_auth_google():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_google'))).click()
    assert driver.current_url.__contains__('accounts.google.com')
    driver.quit()


# TK-16: Авторизация пользователя с помощью учетной записи Yandex
# В режиме инкогнито открытие страница происходит только при повторном клике (БАГ?)
def test_auth_yandex():
    driver, wait = get_driver()
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_ya'))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.ID, 'oidc_ya'))).click()
    assert driver.current_url.__contains__('passport.yandex.ru')
    driver.quit()


# ТК-17: Переход по ссылкам Пользовательское соглашения и Политика конфиденциальности
# Ссылка с Политикой конфиденциальности ведет на Пользовательское соглашение (БАГ?)
def test_open_link_agreement_and_policy():
    driver, wait = get_driver()
    originalWindow = driver.current_window_handle
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'пользовательского соглашения'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break
    window_title = driver.execute_script("return window.document.title")
    assert window_title == 'User agreement'
    driver.close()

    driver.switch_to.window(originalWindow)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break
    window_title = driver.execute_script("return window.document.title")
    assert window_title == 'Privacy Policy'
    driver.close()

    driver.switch_to.window(originalWindow)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]'))).click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != originalWindow:
            driver.switch_to.window(window_handle)
            break
    window_title = driver.execute_script("return window.document.title")
    assert window_title == 'User agreement'
    driver.quit()
