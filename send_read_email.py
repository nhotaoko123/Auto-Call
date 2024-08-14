import imaplib
import smtplib
import email
from email.header import decode_header
from email.message import EmailMessage
from write_read_json import read_data, store_data, WriteInBox
import config as cf
import time
import os

# Email configuration
sender_email = cf.SENDER_EMAIL
password_email = cf.PASSWORD_EMAIL
receiver_email = cf.RECEIVER_EMAIL
subject = cf.SUBJECT
message = cf.MESSAGE
body = cf.BODY
host = cf.HOST
filter = cf.FILTER

class EMAIL():
    def read_email_from_gmail(n1):
        mail = imaplib.IMAP4_SSL(host)
        mail.login(sender_email, password_email)
        mail.select("INBOX")
        _, selected_mails = mail.search(None, filter)
        latest_email_id = selected_mails[0].split()[-1]

        #total number of mails from specific user
        total_mess = len(selected_mails[0].split())

        # Create a directory to save attachments
        save_dir = 'attachments'
        os.makedirs(save_dir, exist_ok=True)
        status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = msg_data[0][1]
        email_message = email.message_from_bytes(raw_email)

        # Extract attachments
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            filename = decode_header(filename)[0][0]
            if isinstance(filename, bytes):
                filename = filename.decode('utf-8')
            
            if filename:
                filepath = os.path.join(save_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                print("Saved attachment:", filename)
        mail.close()
        mail.logout()

        return [email_message['subject'], filename, total_mess]

    def send_email(subject, body, sender, recipients, password, path_attachment=None, path_html=None, html_email=False, html_template_email=False, attachment_email=False):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients
        msg.set_content(body)

        if html_template_email:
            html = open("email_template/sorry_email.html", encoding="utf8")
            text = html.read()
            msg.set_content(text, subtype='html')

        if attachment_email:
            attachment = open(path_attachment, "rb")
            msg.add_attachment(attachment.read(), maintype='application', subtype='octet-stream', filename=attachment.name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
            smtp_server.close()
        WriteInBox('Email sent!')

    def check_new_email(file_path):
        latest_email_id = ""
        file_name = 'total_mess.p'
        save_dir = 'attachments'
        mail = imaplib.IMAP4_SSL(host)
        mail.login(sender_email, password_email)
        total_mess = read_data(file_name)
        while True:
            mail.select("INBOX", readonly=True)
            _, selected_mails = mail.search(None, filter)
            actual_mess = len(selected_mails[0].split())
            if selected_mails[0].split()[-1] == latest_email_id:
                time.sleep(120)
            else:
                latest_email_id = selected_mails[0].split()[-1]
                if actual_mess > int(total_mess):
                    status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
                    raw_email = msg_data[0][1]
                    email_message = email.message_from_bytes(raw_email)

                    # Extract attachments
                    for part in email_message.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue

                        filename = part.get_filename()
                        filename = decode_header(filename)[0][0]
                        if isinstance(filename, bytes):
                            filename = filename.decode('utf-8')
                        
                        if filename:
                            filepath = os.path.join(save_dir, file_path)
                            with open(filepath, 'wb') as f:
                                f.write(part.get_payload(decode=True))
                    store_data(str(actual_mess), file_name)
                    WriteInBox('Have new email')
                    return True

#EMAIL.send_email(subject,body,sender_email,receiver_email,password_email,html_template_email=True)
#EMAIL.check_new_email()