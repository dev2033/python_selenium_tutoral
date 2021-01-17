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

# headless mode
# options.add_argument("--headless")
# options.headless = True

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
    time.sleep(5)
    print("Авторизация успешна")

    news_link = driver.find_element_by_id("l_pr").click()
    time.sleep(5)
    print("Нажатие на профиль")

    video_block = driver.find_element_by_class_name(
        "page_post_sized_thumbs"
    ).click()
    time.sleep(15)
    print("Конец видео")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
