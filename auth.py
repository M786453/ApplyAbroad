
from creds import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class Auth:

    def __init__(self):
        
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*, application/json",
        "Accept-Language": "en-US,en;q=0.9"
        }


    def login(self):

        print("")
        print("Logging In...")
        print("")

        # Setup chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://accounts.applyboard.com")

        driver.find_element(By.ID, "okta-signin-username").send_keys(username)
        driver.find_element(By.ID, "okta-signin-password").send_keys(password)
        driver.find_element(By.ID, "okta-signin-submit").click()

        time.sleep(10)
        
        cookies = driver.get_cookies()

        self.mCookies = dict()
        
        for cookie in cookies:

            if "_applyboard_session" == cookie["name"]:

                self.mCookies["_applyboard_session"] = cookie["value"]

            if "datadome" == cookie["name"]:

                self.mCookies["datadome"] = cookie["value"]

                
        print(self.mCookies)

        driver.quit()

        print("Log In Successful.")
        print("")

Auth().login()