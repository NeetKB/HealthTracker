import pytest
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

