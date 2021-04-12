from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'AppiumP',
            'app':'/Users/venki/Documents/app-debug.apk',
            'appPackage': 'codepath.apps.demointroandroid',
            'appActivity': 'codepath.apps.demointroandroid.DemoSelector'
        }
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
