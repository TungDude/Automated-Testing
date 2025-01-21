from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_mobile_href(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    try:
        # links = WebDriverWait(driver, 10).until(
        #     lambda driver: (
        #         driver.find_elements(By.TAG_NAME, 'a')
        #     )
        # )

        # for link in links:
        #     href = link.get_attribute("href")
        #     response = requests.get(href)

        #     assert response.status_code == 200, f"{href} failed with status code {response.status_code}"

        ios_link, android_link = WebDriverWait(driver, 10).until(
            lambda driver: (
                driver.find_element(By.CSS_SELECTOR, '[data-testid="ios-download"]'),
                driver.find_element(By.CSS_SELECTOR, '[data-testid="android-download"]')
            )
        )

        ios_link = ios_link.get_attribute("href")
        android_link = android_link.get_attribute("href")

        response = requests.get(ios_link)
        assert response.status_code == 200, f"iOS Request failed with status code: {response.status_code}"

        response = requests.get(android_link)
        assert response.status_code == 200, f"Android Request failed with status code: {response.status_code}"

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_href(setup_browser):
    check_mobile_href(setup_browser)