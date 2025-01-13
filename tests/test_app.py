
from playwright.sync_api import expect, Page
from lib.database_connection import DatabaseConnection, get_flask_database_connection
from app import get_flask_database_connection, app

""" Test that page renders successfully"""
def test_render_homepage_successfully(page):
    page.goto('http://127.0.0.1:5000/')
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")
    input_email_tag = page.get_by_text("email")
    expect(input_email_tag).to_be_visible()
    input_password_tag = page.get_by_text("Password")
    expect(input_password_tag).to_be_visible()
    submit_button_tag = page.locator("button[type='submit']")
    expect(submit_button_tag).to_have_text("Register")


""" Test to check user can register successfully"""
def test_homepage_registration(page):
    with app.app_context():
        conn = DatabaseConnection(test_mode=False)
        conn.connect()
        
        # Delete users with the test email
        conn.execute("DELETE FROM users WHERE email = %s", ['cj@example.com'])
        
    page.set_default_timeout(30000)

    page.goto('http://127.0.0.1:5000/')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Carrie John')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("cj@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("pasw0rd!2#")
    
    page.click("button[type='submit']")
    
    expect(page).to_have_url('http://127.0.0.1:5000/register_success') 

    """ Test to check URL remains the same when user provides invalid email"""
def test_email_invalid_error(page ):
    page.set_default_timeout(1000)

    page.goto('http://127.0.0.1:5000/')
   

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Tony Stark')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("tsexample.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("pasw0rd!2#")

    page.click("button[type='submit']")

    expect(page).to_have_url('http://127.0.0.1:5000/')

""" Test to check URL remains the same when user provides invalid password"""
def test_password_invalid_error(page ):
    page.set_default_timeout(1000)

    page.goto('http://127.0.0.1:5000/')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Tony Stark')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("ts@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("pasw")

    page.click("button[type='submit']")

    expect(page).to_have_url('http://127.0.0.1:5000/')

    """ Test to check URL remains the same when user provides duplicate email"""
def test_duplicate_email_error(page ):
    page.set_default_timeout(1000)

    page.goto('http://127.0.0.1:5000/')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Tony Stark')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("ts@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("pasw")

    page.click("button[type='submit']")

    expect(page).to_have_url('http://127.0.0.1:5000/')

""" Test to check URL remains the same when user doesn't provide info"""
def test_no_info_entered_error(page ):
    page.set_default_timeout(1000)

    page.goto('http://127.0.0.1:5000/')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill(' ')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("")

    page.click("button[type='submit']")

    expect(page).to_have_url('http://127.0.0.1:5000/')