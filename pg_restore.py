import argparse
import os

""" 
Comment 

# python3 pg_restore.py -b 1cv82_test -p /mnt/backup/1cv82.gz
Create new base and restore from backup file

"""

username = 'postgres'
backup_file = ''

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base', type=str, help="Input name for new base")
parser.add_argument('-p', '--path', type=str, help="Input path for backup of base")
parse = parser.parse_args()
base = parse.base
backup_file = parse.path

try:
    os.system('unzip ' + backup_file)
except FileExistsError:
    print("File " + backup_file + "doesn't exist")
try:
    os.system('createdb --username postgres -T template0 ' + base)
except:
    print("Created base " + base)
try:
    os.system('psql -U postgres ' + base + ' < ' + backup_file[:-3])
except:
    print("Base " + base + " restored")

try:
    os.remove(backup_file[:-3])
    print("Operation complete")
except:
    print("Operation complete")