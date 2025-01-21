from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import requests

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_request():
    """Verify status code"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Request failed with status code: {response.status_code}"

def check_nocnoc_components(setup_browser):
    """Verify that nocnoc components is present"""
    driver = setup_browser  # Now using the fixture as the driver
    driver.get(BASE_URL)

    try:
        # Wait for the main components to be present
        nocnoc_logo, search_bar, product_container, login_btn = WebDriverWait(driver, 10).until(
            lambda driver: (
                driver.find_element(By.CSS_SELECTOR, '[data-testid="nocnoc-logo"]'),
                driver.find_element(By.CLASS_NAME, 'main-search'), 
                driver.find_element(By.CLASS_NAME, 'product-list'), 
                driver.find_element(By.CSS_SELECTOR, '[data-testid="login-btn"]'),
            )
        )

        # print(nocnoc_logo.get_attribute("outerHTML"))
        # print(search_bar.get_attribute("outerHTML"))
        
        # Verify that both elements are found
        assert nocnoc_logo is not None, "NocNoc logo not found"
        assert search_bar is not None, "Search bar not found"
        assert product_container is not None, "Product container not found"
        assert login_btn is not None, "Login button not found"
    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_init_page(setup_browser):
    check_request()
    check_nocnoc_components(setup_browser)