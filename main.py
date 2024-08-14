from send_read_email import EMAIL
from write_read_json import isEmpty, move_file, read_from_csv, write_to_csv, WriteInBox, read_data, store_data, remove_file_in_folder
from GSM_send_receive import start_call
from LCD import display
from multithread import CustomThread
from GSM_keys import check_phone_number
from upload import upload_file
import config as cf
from date_time import phrase_date_time
import os

path = cf.PATH
inprogress_path = cf.INPROGRESS_PATH
file_name = cf.FILE_NAME
file_output_name = cf.FILE_OUTPUT_NAME
data = cf.DATA
receive_email = cf.RECEIVER_EMAIL
path_done = cf.DONE_PATH
path_file_send = path_done + file_output_name
path_file_upload = inprogress_path + file_output_name


def action_mak_call():
    if not isEmpty(path):
        move_file(path, inprogress_path)
    if not isEmpty(inprogress_path):
        data = read_from_csv(inprogress_path+file_name, toList=True)
    if data != '':
        i = int(read_data('stt.p'))
        while i < len(data):
            phone_number = check_phone_number(data[i][1])
            LCD = display.display_to_LCD(receive_email, data[i][0], file_name)
            response = start_call(phone_number)
            WriteInBox(f'Response from customer => {response}', f'Make phone call to {phone_number}')
            data[i] += [response]
            print(data[i])
            write_to_csv(inprogress_path+file_output_name, data[i], 'a')
            i = i + 1
            store_data(i, 'stt.p')
        store_data(0, 'stt.p')
        upload_file(path_file_upload, phrase_date_time(cf.CLIENT_EMAIL))
        EMAIL.send_email(cf.SUBJECT, cf.BODY, cf.SENDER_EMAIL, cf.RECEIVER_EMAIL, cf.PASSWORD_EMAIL, path_file_upload, html_template_email=True, attachment_email=True)
        remove_file_in_folder(inprogress_path)

if __name__ =="__main__":

    LCD = display.display_to_LCD(receive_email, data, file_name)
    while True:
        check_email = CustomThread(target=EMAIL.check_new_email, args=(file_name,))
        make_call = CustomThread(target=action_mak_call, args=())
        check_email.start()
        new_email = check_email.join()
        if new_email: 
            if not make_call.is_alive():
                make_call.start()
                new_email = False

                