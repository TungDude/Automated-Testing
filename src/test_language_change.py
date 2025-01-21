from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"


def check_eng_language_change(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    try:
        lang_btn = WebDriverWait(driver, 10).until(
            # driver.find_element(By.CSS_SELECTOR, '[data-testid="language-btn"]')
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="language-btn"]'))
        )

        # current_lang = "ไทย" if current_lang.get_attribute("lang") == "th" else "EN"

        lang_btn.click()
        time.sleep(1)

        eng_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div/div[4]/div[3]/div/div[2]')
        eng_button.click()

        body = WebDriverWait(driver, 10).until(
            # driver.find_element(By.CSS_SELECTOR, '[data-testid="language-btn"]')
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        # body = driver.find_element(By.TAG_NAME, 'body')
        assert body.get_attribute("lang").casefold() == "en", "Failed to switch to eng"

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_language_change(setup_browser):
    check_eng_language_change(setup_browser)