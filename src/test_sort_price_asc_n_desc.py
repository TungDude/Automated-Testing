from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_price_sort_asc(setup_browser):
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
        ascend_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='option' and contains(., 'ราคา: จากน้อย-มาก')]"))
        )

        ascend_option.click()
        time.sleep(1)

        # get product container
        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
        )

        # get products list
        children = product_container.find_elements(By.XPATH, './div')
        
        current_price = -999.00
        for child in children:
            price = float(('').join(child.find_element(By.CLASS_NAME, 'offer').text.strip("฿").split(',')))
            assert price >= current_price, "Price not in ascending order"

            current_price = price

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def check_price_sort_desc(setup_browser):
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

        # Get desc option
        descend_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='option' and contains(., 'ราคา: จากมาก-น้อย')]"))
        )

        descend_option.click()
        time.sleep(1)

        # get product container
        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
        )

        # get products list
        children = product_container.find_elements(By.XPATH, './div')
        
        current_price = 2147483647
        for child in children:
            price = float(('').join(child.find_element(By.CLASS_NAME, 'offer').text.strip("฿").split(',')))
            assert price <= current_price, "Price not in descending order"

            current_price = price

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_sort_price_asc_n_desc(setup_browser):
    check_price_sort_asc(setup_browser)
    setup_browser.refresh()
    check_price_sort_desc(setup_browser)