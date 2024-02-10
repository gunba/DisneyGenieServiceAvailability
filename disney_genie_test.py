import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # Initialize UiAutomator2Options with proper capabilities
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.device_name = 'Pixel_3a_API_34_extension_level_7_x86_64'
        options.app_package = 'com.disney.wdw.android'
        options.app_activity = 'com.disney.wdpro.ma.orion.ui.hub.OrionHubActivity'  # Updated activity
        options.no_reset = True  # Correctly apply noReset capability

        # Initialize the Appium driver with the updated options
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_book_experience(self) -> None:
        # Find all elements with "Book Experience" in their content-desc
        book_experience_elements = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 
                                                             'new UiSelector().className("android.view.View").descriptionContains("Book Experience")')

        for element in book_experience_elements:
            # Print the content-desc of each bookable experience found
            print(element.get_attribute("content-desc"))

if __name__ == '__main__':
    unittest.main()