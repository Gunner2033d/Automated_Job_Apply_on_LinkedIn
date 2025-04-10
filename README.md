# 🤖 LinkedIn Auto Job Apply Bot

An automation tool built with Selenium to streamline the job application process on LinkedIn. This script automatically logs into your LinkedIn account and applies to jobs that support the "Easy Apply" feature.

## 📌 Features

- Logs in using secure credentials (via `.env` file)
- Searches for Python Developer roles with custom filters
- Automatically fills out phone number (if missing)
- Applies to jobs with a single click (Easy Apply only)
- Skips complex multi-step applications
- Handles exceptions gracefully
- Saves your time and effort in applying to multiple jobs

## 🚀 How It Works

1. Launches Chrome browser with a specified job search URL
2. Logs in to LinkedIn using provided credentials
3. Iterates through all job listings
4. Applies to each job (if it's a single-step application)
5. Skips complex or non-"Easy Apply" listings
6. Closes the browser after completing all applications

## 🛠️ Tech Stack

- Python
- Selenium
- Python-dotenv
- Chrome WebDriver

## 🔐 Environment Variables

Create a `.env` file in the root directory and add the following:

```env
EMAIL=your_email@example.com
PASSWORD=your_password
PHONE=your_phone_number

```

## 💻 Installation

- git clone https://github.com/Gunner2033d/Automated_Job_Apply_on_LinkedIn
- cd linkedin-auto-apply-bot
- pip install -r requirements.txt





