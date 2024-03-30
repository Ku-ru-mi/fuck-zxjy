import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

cookies = []  # 填入获取到的cookie
zx_url = ""  # 填入学习中心页面的网址

driverPath = ChromeDriverManager().install()
print(driverPath)
# driverPath = "G:\\chromedriver-win32/chromedriver.exe"
jsCode = requests.get(
    "https://gitcode.net/mirrors/requireCool/stealth.min.js/-/raw/main/stealth.min.js?inline=false")。text


def add_js_to_browser(driver):  # 防止网站反爬
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': jsCode})  # 屏蔽selenium参数


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 1}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

service = ChromeService(executable_path=driverPath)

driver = webdriver.Chrome(options=chrome_options, service=service)

add_js_to_browser(driver)  # 每次进入网页前刷入一下屏蔽js


def login():  # 登录
    driver.get(
        url="https://zxjy.zjjtedu.cn/index.php")  # 进入网站

    # 添加 cookie 到 WebDriver
    for cookie in cookies:
        driver.add_cookie(cookie)
    # 刷新页面，使得新的 cookie 生效
    driver.refresh()
    # 进入学习中心
    while 1:
        driver.get(
            url=zx_url)  # 进入网站
        time.sleep(2)
        button = driver.find_element(By.XPATH, '//*[@id="get_my_study_log_html"]/tr[1]/th[6]/a[1]')
        button.click()
        for i in range(600):
            time.sleep(1)
            try:
                button = driver.find_element(By.XPATH, '//*[@id="study_tips"]/a')
                button.click()
            except:
                print("Element not found")
        driver.refresh()


login()
