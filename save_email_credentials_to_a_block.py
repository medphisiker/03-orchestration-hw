import os
from prefect_email import EmailServerCredentials
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
gmail = os.getenv("GMAIL")
app_gmail_password = os.getenv("APP_GMAIL_PASSWORD")
email_name = os.getenv("EMAIL_NAME")

credentials = EmailServerCredentials(
    username=gmail,
    password=app_gmail_password,  # must be an app password
)
credentials.save(email_name)
