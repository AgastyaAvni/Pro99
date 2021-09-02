import os
import shutil
import time 

path='C:\Users\HP\Desktop\WhiteHat\Projects\proc99'

days=60

seconds=time.time()-(days*24 * 60 *60)

if os.path.exists(path):

    for root_folders,folders,files in os.walk(path):
        
        if seconds>=get_file_or_folder_age(root_folder):
            remove_folder(root_folder)
            deleted_folders_count +=1

            break

    else:
        for folder in folders:

            folder_path=os.path.join(root_folder,folder)

            if seconds >= get_file_or_folder_age(folder_path):
                remove_file(path)
                deleted_files_count +=1

                print(f"Total folders deleted: {deleted_folders_count}")
                print(f"Total files deleted: {deleted_files_count}")

def remove_folder(path):


