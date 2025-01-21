from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
import time

# Test Page
BASE_URL = "https://nocnoc.com/pl/All?area=search&st=%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AD%E0%B8%B8%E0%B9%88%E0%B8%99#"

def check_input_out_of_bound(setup_browser):
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

        # sort and store lowest price
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

        children = product_container.find_element(By.XPATH, './div')
        lowest_price = int(float(('').join(children.find_element(By.CLASS_NAME, 'offer').text.strip("฿").split(','))))

        # sort and store highest price
        sort_option_btn.click()

        descend_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='option' and contains(., 'ราคา: จากมาก-น้อย')]"))
        )

        descend_option.click()
        time.sleep(1)

        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
        )

        children = product_container.find_element(By.XPATH, './div')
        highest_price = int(float(('').join(children.find_element(By.CLASS_NAME, 'offer').text.strip("฿").split(','))))

        # refresh and start filtering
        driver.refresh()

        filter_container = WebDriverWait(driver, 10).until(
            lambda driver: (
                driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div/button')
            )
        )
        filter_container.click()
        time.sleep(1)

        price_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div/div[4]/div[1]/div/div[5]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", price_container)
        time.sleep(1)
        price_container.click()
        time.sleep(1)

        low_price_input = price_container.find_element(By.XPATH, './/input[@placeholder="ต่ำสุด"]')
        high_price_input = price_container.find_element(By.XPATH, './/input[@placeholder="สูงสุด"]')

        # input out of bound
        low_price_input.send_keys(str(lowest_price - 100))
        time.sleep(2)
        high_price_input.send_keys(str(highest_price + 100))
        time.sleep(2)

        assert int(low_price_input.get_attribute('value')) == lowest_price, "Price input exceeds lower bound"
        assert int(high_price_input.get_attribute('value')) == highest_price, "Price input exceeds upper bound"

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def check_filter_price(setup_browser):
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

        # sort and store lowest price
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

        children = product_container.find_element(By.XPATH, './div')
        lowest_price = int(float(('').join(children.find_element(By.CLASS_NAME, 'offer').text.strip("฿").split(','))))

        # sort and store highest price
        sort_option_btn.click()

        descend_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='option' and contains(., 'ราคา: จากมาก-น้อย')]"))
        )

        descend_option.click()
        time.sleep(1)

        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
        )

        children = product_container.find_element(By.XPATH, './div')
        highest_price = int(float(('').join(children.find_element(By.CLASS_NAME, 'offer').text.strip("฿").split(','))))

        # refresh and start filtering
        driver.refresh()

        filter_container = WebDriverWait(driver, 10).until(
            lambda driver: (
                driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div/button')
            )
        )
        filter_container.click()
        time.sleep(1)

        price_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div/div[4]/div[1]/div/div[5]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", price_container)
        time.sleep(1)
        price_container.click()
        time.sleep(1)

        low_price_input = price_container.find_element(By.XPATH, './/input[@placeholder="ต่ำสุด"]')
        high_price_input = price_container.find_element(By.XPATH, './/input[@placeholder="สูงสุด"]')

        # normal price input
        input_low = lowest_price + (highest_price - lowest_price) // 4
        low_price_input.send_keys(str(input_low))
        time.sleep(2)
        input_high = highest_price - (highest_price - lowest_price) // 4
        high_price_input.send_keys(str(input_high))
        time.sleep(2)

        assert int(low_price_input.get_attribute('value')) is not None, "Lower bound price filter is not working"
        assert int(high_price_input.get_attribute('value')) is not None, "Upper bound price filter is not working"

        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-list'))
        )

        children = product_container.find_elements(By.XPATH, './div')
        for child in children:
            price = float(('').join(child.find_element(By.CLASS_NAME, 'offer').text.strip("฿").split(',')))
            assert price >= input_low and price <= input_high, "Product does not belong in this price filter."

    except Exception as e:
        pytest.fail(f"Base URL test failed in Selenium: {str(e)}")

def test_filter_price(setup_browser):
    check_input_out_of_bound(setup_browser)
    setup_browser.refresh()
    check_filter_price(setup_browser)