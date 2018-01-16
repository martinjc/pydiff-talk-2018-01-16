import os

# _credentials.py should contain a valid username and password
# for accessing the email server (SMTP_SERVER) given below. It's
# in the .gitignore so it won't get added to the Git repo during
# development
from _credentials import uname, pwd

# Address to send emails from
SEND_FROM = "chorleymj@cardiff.ac.uk"

# details for the email server
SMTP_SERVER = "outlook.office365.com"
SMTP_PORT = 587
SMTP_USERNAME = uname
SMTP_PASSWORD = pwd
