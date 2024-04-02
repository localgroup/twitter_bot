from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

TWITTER_EMAIL = "YOUR REGISTERED E-MAIL"
TWITTER_PASSWORD = "YOUR TWITTER LOGIN PASSWORD"

# Make sure you have a very fast internet connection, if you want to reduce the time.sleep(x) value!!!


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.upload = 0
        self.download = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        accept_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()
        time.sleep(5)

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)
        self.upload = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.download = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"{self.download} and {self.upload}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        # Wait for the button to be clickable
        wait = WebDriverWait(self.driver, 10)

        def agree():
            try:
                agree_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and contains(@class, 'css-175oi2r')]")))
                agree_button.click()
            except:
                pass

        agree()
        time.sleep(10)

        def sign():
            try:
                sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span')))
                sign_in.click()
            except:
                pass

        sign()
        time.sleep(10)

        def email():
            enter_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
            time.sleep(3)
            enter_email.send_keys(TWITTER_EMAIL)

        email()
        time.sleep(10)

        def next_b():
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')))
            next_button.click()

        next_b()
        time.sleep(10)

        def password():
            password_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
            time.sleep(3)
            password_button.send_keys(TWITTER_PASSWORD)

        password()
        time.sleep(10)

        def log_in():
            log_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')))
            time.sleep(3)
            log_in_button.click()

        log_in()
        time.sleep(50)

        def post_initiate():
            try:
                post_initiate_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg')))
                time.sleep(3)
                post_initiate_button.click()

            except:
                pass

        time.sleep(5)
        post_initiate()

        def post_entry():
            post_entry_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
            time.sleep(3)
            tweet = f"Hey @YOUR_ISP, why is my internet speed {self.download}⬇️/{self.upload}⬆️ ?"
            post_entry_button.send_keys(tweet)

        time.sleep(5)
        post_entry()

        def post():
            post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')))
            time.sleep(3)
            post_button.click()

        time.sleep(5)
        post()
        time.sleep(5)

        def if_asked_twitter():
            try:
                got_it = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/span/span')))
                time.sleep(3)
                got_it.click()

            except:
                pass

        time.sleep(20)
        if_asked_twitter()
        time.sleep(10)

        def log_out_initiate():
            try:
                log_out_button_initiate = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]/div')))
                time.sleep(3)
                log_out_button_initiate.click()

            except:
                pass

        time.sleep(5)
        log_out_initiate()
        time.sleep(3)

        def log_out_click():
            try:
                log_out_click_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div/span')))
                time.sleep(3)
                log_out_click_button.click()

            except:
                pass

        time.sleep(5)
        log_out_click()
        time.sleep(5)

        def log_out():
            try:
                log_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')))
                time.sleep(3)
                log_out_button.click()

            except:
                pass

        time.sleep(3)
        log_out()

        def quit_browser():
            self.driver.quit()

        time.sleep(20)
        quit_browser()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
