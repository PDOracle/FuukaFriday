import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from os import mkdir, listdir
from os.path import join
from datetime import date
import urllib.request


class PostPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "latestTab": ('XPATH', '//*[@role="tablist"]//child::span[text() = "Latest"]'),
        "body": ('TAG', 'body'),
    }

    def checkLatest(self):
        time.sleep(2)
        self.latestTab.click()

    def latestExists(self) -> bool:
        return self.latestTab.is_displayed()

    def createFolder(self, name, parent):
        created_folders = listdir(parent)
        if name not in created_folders:
            mkdir(join(parent, name))
            print("New folder " + name + " has been created!")

    def downloadFile(self, url, fpath, fname, ftype):
        if ftype == "i":
            full_path = fpath + "\\" + fname + ".jpg"
            urllib.request.urlretrieve(url, full_path)
        if ftype == "v":
            full_path = fpath + "\\" + fname + ".mp4"
            urllib.request.urlretrieve(url, full_path)

    def loadPosts(self):
        posts_seen = []
        current_date = date.today()
        download_path = 'C:\\Users\\Leafk\\Desktop\\ItsFuukaFriday'
        hitImages = '//img[contains(@src, "https://pbs.twimg.com/media")]'
        hitVideos = '//video[contains(@src, "https://video.twimg.com")]'
        self.createFolder(str(current_date), download_path)
        for i in range(20):
            self.body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            img_fuukas = self.driver.find_elements(By.XPATH, hitImages)
            vid_fuukas = self.driver.find_elements(By.XPATH, hitVideos)
            for img in img_fuukas:
                fuuka_link = img.get_attribute('src')
                if fuuka_link not in posts_seen:
                    posts_seen.append(fuuka_link)
                    self.downloadFile(fuuka_link, join(download_path, str(current_date)), str(len(posts_seen)), "i")
            for vid in vid_fuukas:
                fuuka_link = vid.get_attribute('src')
                if fuuka_link not in posts_seen:
                    posts_seen.append(fuuka_link)
                    self.downloadFile(fuuka_link, join(download_path, str(current_date)), str(len(posts_seen)), "v")
        time.sleep(2)

        for fuuka_link in posts_seen:
            print(fuuka_link + "\n")