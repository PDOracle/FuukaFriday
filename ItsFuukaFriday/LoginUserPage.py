import time
from seleniumpagefactory.Pagefactory import PageFactory


class UserPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    username = "[-> INSERT USERNAME HERE <-]"

    locators = {
        "user": ('NAME', 'text'),
        "nextBtn": ('XPATH', "//span[text() = 'Next']")
    }

    def login_user(self):
        time.sleep(3)
        self.user.set_text(self.username)
        self.nextBtn.click()
