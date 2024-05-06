import time

from seleniumpagefactory.Pagefactory import PageFactory


class PassPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    password = "[-> INSERT PASSWORD HERE <-]"

    locators = {
        "pw": ('NAME', 'password'),
        "loginBtn": ('XPATH', "//span[text() = 'Log in']")
    }

    def loginPass(self):
        time.sleep(2)
        self.pw.set_text(self.password)
        self.loginBtn.click()
