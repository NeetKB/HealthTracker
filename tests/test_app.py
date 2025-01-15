
from playwright.sync_api import expect, Page
from lib.database_connection import DatabaseConnection, get_flask_database_connection
from app import get_flask_database_connection, app


### HOMEPAGE/REGISTRATION TESTS ###
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
def test_email_invalid_error(page):
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
def test_duplicate_email__URL_stays_same(page ):
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
def test_no_info_entered_URL_stays_same(page ):
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

    """ Test to check login link (at the bottom) works"""
def test_login_link_works(page ):
    page.set_default_timeout(1000)

    page.goto('http://127.0.0.1:5000/')


    page.click("a[href='/login']")

    expect(page).to_have_url('http://127.0.0.1:5000/login')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Log into your Health Tracker account")


""" Test error appears when password w/o special characters is given"""
def test_error_shown_when_password_wo_special_chars_given(page):
    page.set_default_timeout(1000)
    page.goto('http://127.0.0.1:5000/')

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Sam John')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("sj@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("paord123")

    page.click("button[type='submit']")
    
    h4_tag = page.locator("h4")
    expect(h4_tag).to_have_text("This password does not comply with requirements! Must have at least one special character.")

""" Test error appears when password length is incorrect"""
def test_error_shown_when_password_length_of_password_given(page):
    page.set_default_timeout(1000)
    page.goto('http://127.0.0.1:5000/')

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Sam John')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("sj@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("pa123")

    page.click("button[type='submit']")
    
    h4_tag = page.locator("h4")
    expect(h4_tag).to_have_text("This password does not comply with requirements! Must have at least 8 characters.")

""" Test error appears when email is already in use"""
def test_error_shown_when_email_already_in_use(page):
    page.set_default_timeout(1000)
    page.goto('http://127.0.0.1:5000/')

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Sam John')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("sam@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("passs123!")

    page.click("button[type='submit']")
    
    h4_tag = page.locator("h4")
    expect(h4_tag).to_have_text("This email is already in use.")



    ### LOGIN TESTS ###

    """ Test to check URL changes when user provides correct info"""
def test_user_can_log_in_with_correct_info(page):
    page.set_default_timeout(1000)
    page.goto('http://127.0.0.1:5000/login')
    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("tgh@test.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("Password123!")
    
    page.click("button[type='submit']")
    expect(page).to_have_url('http://127.0.0.1:5000/dashboard')


""" Test to check URL remains the same when user doesn't provide info"""
def test_user_url_stays_the_same_when_no_info_given(page):
    page.set_default_timeout(1000)
    page.goto('http://127.0.0.1:5000/login')
    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill(" ")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill(" ")
    
    page.click("button[type='submit']")
    expect(page).to_have_url('http://127.0.0.1:5000/login')

    """ Test to check URL stays the same if user provides incorrect info"""
def test_url_stays_the_same_when_user_gives_incorrect_info(page):
    page.set_default_timeout(1000)
    page.goto('http://127.0.0.1:5000/login')
    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("sam@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("paord123!")
    
    page.click("button[type='submit']")
    expect(page).to_have_url('http://127.0.0.1:5000/login')

    """ Test to check registration link works"""
def test_register_link_works(page ):
    page.set_default_timeout(1000)

    page.goto('http://127.0.0.1:5000/login')


    page.click("a[href='/']")

    expect(page).to_have_url('http://127.0.0.1:5000/')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")

""" Test to error appears when password is incorrect"""
def test_error_shown_when_incorrect_info_given(page):
    page.goto('http://127.0.0.1:5000/login')
    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("sam@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("paord123!")

    page.click("button[type='submit']")
    
    h4_tag = page.locator("h4")
    expect(h4_tag).to_have_text("Incorrect email or password")