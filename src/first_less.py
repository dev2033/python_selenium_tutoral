from selenium import webdriver
import time
from fake_useragent import UserAgent

# fake_user agent
user_agent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options2 = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={user_agent.random}")
# options2.set_preference("general.useragent.override", user_agent.random)

driver = webdriver.Chrome(executable_path="/home/proger/Документы/selenium_less"
                                          "/src/chromedriver",
                          options=options)

# driver2 = webdriver.Firefox(
#     executable_path="путь до firefox driver/firefox_driver..",
#     options=options2
# )

url = "https://www.youtube.com/?gl=RU&hl=ru"

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
