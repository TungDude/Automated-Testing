from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_amount_sold_sort(setup_browser):
    driver = setup_browser
    driver.get(BASE_URL)

    try:
        popup_close_btn, sort_option_btn = WebDriverWait(driver, 10).until(
            lambda driver: (
                driver.find_element(By.CLASS_NAME, 'icon-close-new'),
                driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[4]/div[2]/div[1]/div/div/button'),
            )
        )

        popup_close_btn.click()
        time.sleep(1)

        # Check if sort button is displayed
        assert sort_option_btn is not None, "Sort button not found"

        sort_option_btn.click()

        # Get asc option
        amount_sold_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='option' and contains(., 'สินค้าขายดี')]"))
        )

        amount_sold_option.click()
        time.sleep(1)

        # get product container
        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
        )

        # get products list
        children = product_container.find_elements(By.XPATH, './div')
        
        curr_amount_sold = 2147483647.00
        for child in children:
            child_span = child.find_element(By.XPATH, ".//p[span[text()='ขายแล้ว']]")
            child_span = child_span.text.strip('ขายแล้ว').strip()
            have_k = True if "K" in child_span else False
            sold = float(child_span.strip("K")) * (1000 if have_k else 1 )
            
            assert sold <= curr_amount_sold, "Amount sold not in correct order"

            curr_amount_sold = sold

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_sort_amount_sold(setup_browser):
    check_amount_sold_sort(setup_browser)