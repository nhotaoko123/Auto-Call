PATH = './attachments/'
INPROGRESS_PATH = './task_inprogress/'
DONE_PATH = './task_done/'
FILE_NAME = 'data.csv'
FILE_OUTPUT_NAME = 'data_output.csv'
DATA = ''


SENDER_EMAIL = 'maketingtoolsms@gmail.com'
PASSWORD_EMAIL = 'cjmgabhiepqvlzie'
CLIENT_EMAIL = "phamvanduy0914@gmail.com"
RECEIVER_EMAIL = [CLIENT_EMAIL]
SUBJECT = 'Subject of the email'
MESSAGE = 'This is the body of the email.'
BODY = "This is the body of the text message"
PATH_ATTACHMENT = 'attachments/data_out.csv'
HOST = "imap.gmail.com"
KEY = "Hello world"
FILTER = f'(Subject "{KEY}") (FROM "{RECEIVER_EMAIL}")'


SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'client_secret.json'
PARENT_FOLDER_ID = "1sqSGkBnxiaris0w-ZSrLRCdGlOT-pyiF"
