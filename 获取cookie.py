import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driverPath = ChromeDriverManager().install()
print(driverPath)
#driverPath = "G:\\chromedriver-win32/chromedriver.exe"
jsCode = requests.get(
    "https://gitcode.net/mirrors/requireCool/stealth.min.js/-/raw/main/stealth.min.js?inline=false").text


def add_js_to_browser(driver):  # 防止网站反爬
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': jsCode})  # 屏蔽selenium参数


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 1}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

service = ChromeService(executable_path=driverPath)

driver = webdriver.Chrome(options=chrome_options, service=service)

add_js_to_browser(driver)  # 每次进入网页前刷入一下屏蔽js

# 打开已经登录的网站
driver.get("https://zxjy.zjjtedu.cn/index.php")
input()
cookies = driver.get_cookies()
print(cookies)

# 关闭浏览器窗口
driver.quit()
