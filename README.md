# WORK IN PROGRESS: Health Tracker project

I am commited to web accessibiity and aim to ensure that implementing accessibility elements are at the core of this project.

I plan to make the application accessible by implementing W3C standards & principles [Link for W3C](https://www.w3.org/WAI/fundamentals/)and via customisations (e.g. text size and color contrast).

This application aims to allow users to create an account, sign-in and track the below information and provide weekly, monthly, quarterly and yearly reports:
(see features below for the functunality that has been implemented)

- Symptoms
- Medications
- Glimmers (i.e. positive interactions )
- Actions (i.e. exercise/busy days)
- Habits
- Feelings
- Food

In addition to the above, the user will be able to store:
- Medical conditions 
- Doctors information 
- Reminders 
- Medical appointments
- and notes for any appointments

This appplication is aimed at people with chronic illnesses. The application would be useful to show Doctors how symptoms have progressed / declined over a long period of time, instead of the user relying on memory.

## Built with Python, Flask, PostgreSQL, Pytest and Tailwind CSS.

## 🌟 Features

    * User Authentication: Users can create an account (Passwords are encrypted in the database).

## 🔧 Prerequisites

Ensure you have Python and PostgreSQL installed.This project includes precompiled Tailwind CSS styles. No additional Tailwind installation is required.

Setup for Windows

# Set up the virtual environment

; python -m venv [VENV_NAME] -venv

# Activate the virtual environment

; [VENV_NAME]\Scripts\Activate

# Install dependencies

([VENV_NAME]-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing

([VENV_NAME]-venv); playwright install

# To run the tests (with extra logging)

([VENV_NAME]-venv); pytest -sv

# To run the app

([VENV_NAME]-venv); python app.py

# Now visit http://localhost:5000/ in your browser
