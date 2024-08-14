import logging
import json
import pandas as pd
import csv
import os
import shutil
import pickle


logging.basicConfig(filename="log.log", level=logging.INFO, encoding='utf-8', format='%(asctime)s %(message)s', filemode='a')




file_name = 'store_data.json'
file_csv = 'attachments/data.csv'
file_csv_output = 'attachments/data_out.csv'
file_excel = 'attachments/data.xlsx'

def read_from_json():
   with open(file_name, mode='r', encoding='utf-8') as f:
      data = json.load(f)
      f.close()

   return data

def write_to_json(dictionary):
   with open(file_name, mode='w', encoding='utf-8') as f:
      json.dump(dictionary, f)
      f.close()

   return 'Write to json success'

def update_to_json(dictionary):
   with open(file_name, "r+") as jsonFile:
      data = json.load(jsonFile)
      data.update(dictionary)
      jsonFile.seek(0)  # rewind
      json.dump(data, jsonFile)
      jsonFile.truncate()

   return 'Update to json success'

def read_from_csv(file_csv, toList=False, toDict=False):
   data_dict = {}
   with open(file_csv, 'r') as csv_file:
      if toDict:
         csv_reader = csv.reader(csv_file)
         for row in csv_reader:
            key = row[0]
            value = row
            data_dict[key] = value
         return data_dict
      if toList:
         csv_reader = csv.reader(csv_file)
         data_list = []
         for row in csv_reader:
            value = row
            data_list.append(value)
         return data_list # k = read_from_csv(file_csv,toList=True)  =>> data_list[0][0]
   csv_file.close() 
   
def write_to_csv(file_csv_output, list_data, mode='w'):
   header = ['name', 'area', 'country_code2', 'country_code3']

   if mode == 'w':
      with open(file_csv_output, mode=mode, encoding='UTF8', newline='') as f:
         writer = csv.writer(f)
         # write the header
         writer.writerow(header)
         writer.writerow(list_data)
         f.close()
   if mode == 'a':
      with open(file_csv_output, mode=mode, encoding='UTF8', newline='') as f:
         writer = csv.writer(f)
         # write the data
         writer.writerow(list_data)
         f.close()
   return 'done'

def read_from_excel(file_excel_path):
   #to be updated
   dict = pd.read_excel(file_excel_path)
   dict.to_dict()
   return dict

def move_file(source, destination):
   #source = 'D:/Project/GSM module/attachments'
   #destination = 'D:/Project/GSM module/task_done'
   #
   # gather all files
   allfiles = os.listdir(source)
   
   # iterate on all files to move them to destination folder
   for f in allfiles:
      src_path = os.path.join(source, f)
      dst_path = os.path.join(destination, f)
      shutil.move(src_path, dst_path)

def WriteInBox(result, sTitle=None):
   iMaxLengh = len(result)
   if sTitle:
      isTitleLengh = len(str(sTitle))
      iMaxLengh =  isTitleLengh if iMaxLengh < isTitleLengh else iMaxLengh
    
   logging.info("╔" + ("═"*(iMaxLengh+2)) + "╗")

   if sTitle:
      logging.info(    "║ "+ str(sTitle).center(iMaxLengh)       + " ║")
      logging.info(    "╠═" + ("═"*(iMaxLengh+1))                + "╣")
   
   logging.info("║" + (result).center(iMaxLengh+2) + "║")


   logging.info("╚" + ("═"*(iMaxLengh+2)) + "╝")

def write_to_txt(text, filename):
   filename = "total_mess.txt"
   file1 = open(filename, "w")
   file1.write(text)
   file1.close()

def read_from_txt(filename):
   filename = "total_mess.txt"
   file1 = open(filename, "r+")
   result = file1.read()
   file1.close()
   return result

def store_data(data, filename):
   file = open(filename, 'wb')
   pickle.dump(data, file)
   file.close()

def read_data(filename):
   file = open(filename, 'rb')
   data = pickle.load(file)
   file.close()
   return data

def isEmpty(path):
   if os.path.exists(path) and not os.path.isfile(path):
  
        # Checking if the directory is empty or not
      if not os.listdir(path):
         return True
      else:
         return False
   else:
      return True
   
def remove_file_in_folder(folder_path):
   # List all files in the folder
   files = os.listdir(folder_path)
   # Iterate through the files and delete them
   for file in files:
      file_path = os.path.join(folder_path, file)

      # Check if the path is a file (not a directory) before deleting
      if os.path.isfile(file_path):
         os.remove(file_path)
         print(f"Deleted: {file_path}")