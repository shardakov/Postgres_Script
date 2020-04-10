import os
import argparse
try:
    from os import scandir
except ImportError:
    from scandir import scandir

"""
Comment

# python3 rm_backup_by_date.py -p */path/*
WARNING!!! This script save last 7 backups(files)
in our case is /mnt/backup/*/
python3 /root/pgsql_script/rm_backup_by_name.py -p /mnt/backup/sermifff_bases_91_103/

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
    my_files = [f.name for f in scandir(i) if f.is_file()]
    for file in sorted(my_files, reverse=True)[3:]:
        if file[-5:] != '01.gz':
            os.remove(i + "/" + file)
