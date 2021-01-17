from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent

from settings import vk_login, vk_password

import time
import pickle


# fake_user agent
user_agent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")

driver = webdriver.Chrome(
    executable_path="/home/proger/Документы/selenium_less"
                    "/src/chromedriver",
    options=options
)

url = "https://vk.com/"


def save_cookies():
    """Сохраняет куки"""
    driver.get(url=url)
    time.sleep(5)

    email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys(vk_login)
    time.sleep(2)

    password = driver.find_element_by_id("index_pass")
    password.clear()
    password.send_keys(vk_password)
    time.sleep(1)
    # Клавиша Enter
    password.send_keys(Keys.ENTER)

    # Кнопка логина в ВК
    # login_button = driver.find_element_by_id("index_login_button").click()

    time.sleep(5)

    news_link = driver.find_element_by_id("l_nwsf").click()
    time.sleep(5)

    # cookies
    pickle.dump(driver.get_cookies(), open(f"{vk_login}_cookies", "wb"))


def load_cookie_vk():
    """Загружает куки"""
    driver.get("https://vk.com/")

    for cookie in pickle.load(open(f"{vk_login}_cookies", "rb")):
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()
    time.sleep(5)


try:
    """Расскоментить и закоментить эти фунции по порядку"""
    # для начала сохраним куки
    # save_cookies()

    # затем вызываем эту функцию
    # load_cookie_vk()


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
