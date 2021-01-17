from selenium import webdriver

from fake_useragent import UserAgent

import time


# fake_user agent
user_agent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")

# disable webdriver

# for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/home/proger/Документы/selenium_less"
                    "/src/chromedriver",
    options=options
)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/"
               "chrome-headless-test.html")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
