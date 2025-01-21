from selenium.webdriver.common.by import By
import time
import pytest

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_seo_elements(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    try:
        time.sleep(3)

        # check title
        title = driver.title
        assert title, "Title is not present"

        # check meta description
        meta_description = driver.find_element(By.CSS_SELECTOR, "meta[name='description']")
        assert meta_description, "Meta description tag is missing"

        # check meta keywords
        meta_keywords = driver.find_element(By.CSS_SELECTOR, "meta[name='keywords']")
        assert meta_keywords, "Meta keywords tag is missing"

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_seo_elements(setup_browser):
    check_seo_elements(setup_browser)