from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent

from settings import vk_login, vk_password

import time


# fake_user agent
user_agent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/home/proger/Документы/selenium_less"
                    "/src/chromedriver",
    options=options
)


url = "https://vk.com/"

try:
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

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
