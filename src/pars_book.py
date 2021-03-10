from selenium import webdriver
import time
from fake_useragent import UserAgent


user_agent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")

driver = webdriver.Chrome(
    executable_path="/home/danil/Documents/"
    "python_selenium_tutorial/"
    "src/chromedriver",
    options=options
)

url = "https://www.surgebook.com/daniil_sh/book/osnovy-ib-na-python1/vvedenie"

try:
    # переходи по стриницам
    driver.get(url=url)
    time.sleep(5)
    # делает скриншот страницы
    # driver.get_screenshot_as_file("скрин.png")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

