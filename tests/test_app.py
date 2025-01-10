from playwright.sync_api import expect, Page

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
def test_homepage_registration(page ):
    page.set_default_timeout(1000)

    page.goto('http://127.0.0.1:5000/')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register an account")

    input_fullname_tag = page.locator("input[name='fullname']")
    input_fullname_tag.fill('Bobby')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("bobby@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("pasw0rd!2#")
 
    page.click("button[type='submit']")
   

    expect(page).to_have_url('http://127.0.0.1:5000/register_success')
  
    