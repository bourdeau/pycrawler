from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import random


class Client():

    def request(self, url: str):
        """
        Make a Selenium Request
        There is not way to get HTTP response code (see https://github.com/seleniumhq/selenium-google-code-issue-archive/issues/141)
        """
        options = Options()
        options.add_argument('-headless')
        driver = Firefox(executable_path='geckodriver', firefox_options=options, log_path="./logs/geckodriver.log")
        driver.get(url)
        html = driver.page_source

        # rand = random.randint(0, 5000)
        # driver.save_screenshot('./images/{}.png'.format(str(rand)))
        driver.quit()

        return html
