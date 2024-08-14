CONNECTION = b'AT\r'
ECCHO_COMAND = b'ATEO\r'
SET_SEND_SMS = b'AT+CMGF=1\r'
SET_TEXT_MODE_SMS = b'AT+CMGF=1\r'
SET_RECIEVE_SMS = b'AT+CNMI=2,2,0,0,0\r'
READ_ALL_SMS = b'AT+CMGL="ALL"\r'
READ_UNREAD_SMS = b'AT+CMGL="REC UNREAD"\r'
USB_PORT = '/dev/ttyUSB0'
BRAUCH_RATE = 9600

def send_to(phone_number):
    return b'AT+CMGS="' + phone_number.encode() + b'"\r'

def send_text(text):
    return text.encode() + b"\r"

def make_call(phone_number):
    return  b'ATD' + phone_number.encode() + b';'

def check_phone_number(input_number):
    if len(input_number) == 9 :
        input_number = '+84' + input_number

    if input_number.startswith('0',0, 1):
        input_number = input_number.replace('0', '84', 1)

    if '+' not in input_number:
        input_number = '+' + input_number
    return input_number