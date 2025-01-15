import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from playwright.sync_api import expect, Page

CHROMEDRIVER_PATH = "C:\\Users\\amani\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe" 

# Screen sizes to test
screen_sizes = [
    (1920, 1080),  # Desktop
    (1366, 768),   # Laptop
    (768, 1024),   # Tablet
    (375, 667)     # Mobile
]

url = "http://127.0.0.1:5000/login" 

@pytest.fixture
def driver():
    options = Options()
    #Headless  - the browser operates in the background without opening a visible window on your screen
    options.add_argument("--headless")
    driver_service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service, options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("width, height", screen_sizes)
def test_responsiveness(driver, width, height): 
    driver.get(url)
    driver.set_window_size(width, height)
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log-in')]")
    assert sign_in_button.is_displayed(), f"'Log-in' button is not visible at {width}x{height}"

    
""" Test that page renders successfully"""
def test_render_login_page_successfully(page):
    page.goto('http://127.0.0.1:5000/login')
    h2_tag = page.locator("h2")
    input_email_tag = page.get_by_text("email")
    expect(input_email_tag).to_be_visible()
    input_password_tag = page.get_by_text("Password")
    expect(input_password_tag).to_be_visible()
    submit_button_tag = page.locator("button[type='submit']")
    expect(submit_button_tag).to_have_text("Log-in")