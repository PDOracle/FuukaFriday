import time

from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver


    locators = {
        "searchBar": ('XPATH', '//*[@data-testid = "SearchBox_Search_Input"]'),
    }

    def userSearch(self):
        time.sleep(2)
        self.searchBar.send_keys("fuuka friday")
        self.searchBar.submit()
        time.sleep(1)
