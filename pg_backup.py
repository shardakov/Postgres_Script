import argparse
import os
import time

""" 
Comment 

# python3 pg_backup.py -p /mnt/backup/* -b *,*
Launch with bases.txt without key -b, databases are entered line by line
# python3 pg_backup.py -p /mnt/backup/*
Or launch without key => use default settings
# python3 pg_backup.py

"""

username = 'postgres'
date = time.strftime('%Y-%m-%d')

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, help="Input path for backup", default='')
parser.add_argument('-b', '--bases', type=str, help="Input bases for backup", default='/root/pgsql_script/bases.txt')
parse = parser.parse_args()
backup_dir = parse.path
bases = parse.bases

if bases == '/root/pgsql_script/bases.txt':
    try:
        with open(bases, "r") as file:
            bases = file.read().split("\n")
    except IOError:
        print("can't read from file, IO error")
        exit(1)
else:
    bases = bases.split(",")
for j in bases:
    full_dir = backup_dir + str(j)
    if not os.path.exists(full_dir):
        os.mkdir(full_dir)
    filename = "/%s-%s" % (j, date)
    try:
        os.system('pg_dump --username="' + username
                  + '" --no-password --serializable-deferrable --dbname="' + str(j)
                  + '"  -Z 9 > ' + full_dir + filename + ".gz")
        print("Created backup " + j)
    except FileExistsError as err:
        print(err)