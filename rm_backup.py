import os
import argparse

""" 
Comment 

# python3 rm_backup.py -p */path/*
WARNING!!! This script save last 7 backups(files)
in our case is /mnt/backup/*/

"""

folders = []

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, help="Input path for dir of backup")
parse = parser.parse_args()
backup_dir = parse.path

for root, dirs, files in os.walk(backup_dir):
    for folder in dirs:
        folders.append(os.path.join(root, folder))

for i in folders:
    my_files = [f.name for f in os.scandir(i) if f.is_file()]
    for file in sorted(my_files, key=lambda p: os.path.getctime(os.path.join(i, p)), reverse=True)[7:]:
        os.remove(i + "/" + file)
