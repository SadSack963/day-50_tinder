from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv("E:/Python/EnvironmentVariables/.env")
FACEBOOK_EMAIL = os.getenv("Email_Facebook")
FACEBOOK_PASSWORD = os.getenv("Password_Facebook")


chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
firefox_driver_path = "E:/Python/WebDriver/geckodriver.exe"
opera_driver_path = "E:/Python/WebDriver/operadriver.exe"
driver = webdriver.Firefox(executable_path=firefox_driver_path)


def tinder_login():
    driver.get("https://www.tinder.com")
    sleep(5)
    tinder_handle = driver.current_window_handle
    print(tinder_handle)

    login = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]"
    )
    login.click()
    login_with_facebook()
    driver.switch_to.window(tinder_handle)


def login_with_facebook():
    sleep(5)
    found = False
    print("Looking for Login with Facebook button")
    while not found:
        try:
            facebook = driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button"
            )
            found = True
        except:
            sleep(1)
    facebook.click()
    enter_facebook_details()


def enter_facebook_details():
    # https://www.facebook.com/login.php?skip_api_login=1&api_key=464891386855067&kid_directed_site=0&app_id=464891386855067&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D464891386855067%26cbt%3D1613358347386%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df133128840808e8%2526domain%253Dtinder.com%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff12fa0448098f1c%2526relation%253Dopener%26client_id%3D464891386855067%26display%3Dpopup%26domain%3Dtinder.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Ftinder.com%252F%26locale%3Den_GB%26logger_id%3Df27a4a7fd559fa%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2d778a0152cb44%2526domain%253Dtinder.com%2526origin%253Dhttps%25253A%25252F%25252Ftinder.com%25252Ff12fa0448098f1c%2526relation%253Dopener%2526frame%253Df1a74ec4de864ec%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Duser_birthday%252Cuser_photos%252Cemail%252Cuser_likes%26sdk%3Djoey%26version%3Dv2.8%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2d778a0152cb44%26domain%3Dtinder.com%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff12fa0448098f1c%26relation%3Dopener%26frame%3Df1a74ec4de864ec%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_GB&pl_dbl=0
    sleep(5)
    login_handle = driver.window_handles[1]
    print(login_handle)
    driver.switch_to.window(login_handle)

    print("Looking for Email input box")
    found = False
    while not found:
        try:
            email = driver.find_element_by_id("email")
            found = True
        except:
            sleep(1)

    email.send_keys(FACEBOOK_EMAIL)
    password = driver.find_element_by_id("pass")
    password.send_keys(FACEBOOK_PASSWORD)
    login = driver.find_element_by_id("loginbutton")
    login.click()
    confirm_permissions()


def confirm_permissions():
    # https://www.facebook.com/v2.8/dialog/oauth?app_id=464891386855067&cbt=1613362142328&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1e6af721b972b8%26domain%3Dtinder.com%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff2d0db9b7b2ac86%26relation%3Dopener&client_id=464891386855067&display=popup&domain=tinder.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Ftinder.com%2F&locale=en_GB&logger_id=f4c584d7336118&origin=1&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1d8a553154b72e%26domain%3Dtinder.com%26origin%3Dhttps%253A%252F%252Ftinder.com%252Ff2d0db9b7b2ac86%26relation%3Dopener%26frame%3Df2c662345663532&response_type=token%2Csigned_request%2Cgraph_domain&scope=user_birthday%2Cuser_photos%2Cemail%2Cuser_likes&sdk=joey&version=v2.8&ret=login&fbapp_pres=0&tp=unspecified&ext=1613365748&hash=AeZSN4zBnobtQFPn5Pg
    sleep(5)
    confirm_handle = driver.window_handles[0]
    print(confirm_handle)
    driver.switch_to.window(confirm_handle)

    print("Looking for Continue as button")
    found = False
    while not found:
        try:
            confirm = driver.find_element_by_name("__CONFIRM__")
            found = True
        except:
            sleep(1)
    confirm.click()


tinder_login()
sleep(180)
