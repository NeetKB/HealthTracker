# WORK IN PROGRESS: Health Tracker project

This repository is an application that allows to create an account, sign-in and aims to track the below information and provide weekly, monthly, quarterly and yearly reports:
(see features below for the functunality that has been implemented)

- Symptoms
- Medications
- Glimmers (i.e. positive interactions )
- Habits
- Feelings
- Food

In addition to the above, the user will be able to store their conditions, doctors information and medical appointments, as well as add notes for any appointments.

## Built with Python, Flask, PostgreSQL, Pytest and Tailwind CSS.

## 🌟 Features

    * User Authentication: Users can create an account. Passwords are encrypted in the database.

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
