from selenium import webdriver

from fake_useragent import UserAgent

import time


# fake_user agent
user_agent = UserAgent()

# options
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference(
    "general.useragent.override",
    f"user-agent={user_agent.random}"
)

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

driver = webdriver.Firefox(
    executable_path="/home/cain/PycharmProjects/selenium_python/"
                    "firefoxdriver/geckodriver",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/"
               "chrome-headless-test.html")
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
