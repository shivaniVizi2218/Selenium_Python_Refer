#
import time

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from utilities.screenshots import Screen_shots


@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    # options.headless = True
    # options.add_argument("--incognito")
    options.add_argument("start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--headless')
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--safebrowsing-disable-download-protection")
    prefs = {
        "download.prompt_for_download": False,
        "download.default_directory": os.path.abspath('.') + "\\Downloads"}
    options.add_experimental_option("prefs", prefs)

    service = Service()
    options.add_argument("--disable-popup-blocking") #Required for download
    options.add_argument("--safebrowsing-disable-download-protection") #Required for download
    options.add_argument('--kiosk-printing') #Required for download
    prefs = {
        "download.prompt_for_download": False, #Required for download
        "download.default_directory": os.path.abspath('.') + "\\Downloads"} #Require for download
    options.add_experimental_option("prefs", prefs) #Required for download
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  #when chrome version changes you need to uncomment and run this once
    #service = Service(executable_path="C:/Users/skhan/.wdm/drivers/chromedriver/win64/121.0.6167.85/chromedriver-win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    time.sleep(5)
    return driver

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    driver = item.funcargs['setup']
    screenshots = Screen_shots(driver)
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "@")
            file_name = file_name.replace("/", "@")
            file_list1 = file_name.split("@")
            file_path = screenshots.take_screenshot(driver, file_list1[-1], file_list1[1])
            if file_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path.replace("%20", "%2520")
                extra.append(pytest_html.extras.html(html))
            report.extra = extra