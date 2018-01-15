from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
# import random


class Client():

    def request(self, url: str):
        """
        Make a Selenium Request
        There is not way to get HTTP response code (see https://github.com/seleniumhq/selenium-google-code-issue-archive/issues/141)
        """
        options = Options()
        options.add_argument('-headless')
        browser = Firefox(executable_path='geckodriver', firefox_options=options, log_path="./logs/geckodriver.log")
        browser.get(url)
        # Supposed to render JS http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php
        # innerHTML = browser.execute_script("return document.body.innerHTML")
        html = browser.page_source
        # rand = random.randint(0, 5000)
        # browser.save_screenshot('./images/{}.png'.format(str(rand)))
        browser.quit()

        return html
