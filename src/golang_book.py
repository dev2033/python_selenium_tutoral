import time

from selenium import webdriver
from fake_useragent import UserAgent


user_agent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/home/proger/Документы/python_selenium_tutorial/"
                    "src/chromedriver",
    options=options
)

url = "http://golang-book.ru/chapter-01-gettting-started.html"

try:
    count = 0
    count_file = 0
    driver.get(url=url)
    time.sleep(3)
    for item in range(0, 15):
        content_page = driver.find_element_by_class_name(
            "content_containter"
        ).text
        time.sleep(2)

        with open(f'data_golang/Chapter_{count_file + 1}.txt', 'w') as file:
            file.write(content_page)
        count_file += 1

        time.sleep(2)
        button_next_page = driver.find_element_by_class_name("-next").click()
        time.sleep(3)
        count += 1
        print(f'#{count} is done!')


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

