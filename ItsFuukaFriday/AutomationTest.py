import time
import unittest
from selenium import webdriver
from LoginUserPage import UserPage
from LoginPassPage import PassPage
from UserHomePage import HomePage
from UserPostPage import PostPage


class AutomationTest(unittest.TestCase):

    def test_fullsession(self):
        driver = webdriver.Chrome()
        driver.get("https://twitter.com/i/flow/login")

        userPg = UserPage(driver)
        passPg = PassPage(driver)
        homePg = HomePage(driver)
        postPg = PostPage(driver)

        userPg.login_user()

        passPg.loginPass()

        homePg.userSearch()

        self.assertTrue(postPg.latestExists(), "Latest tab is not displayed correctly.")
        postPg.checkLatest()
        time.sleep(2)
        postPg.loadPosts()

        driver.quit()


if __name__ == '__main__':
    unittest.main()