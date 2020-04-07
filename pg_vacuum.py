import argparse
import os

""" 
Comment 

# python3 pg_vacuum.py -b *,*
Launch vacuum for postgres bases with key VERBOSE, ANALYZE, FREEZE, FULL

"""

username = 'postgres'

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bases', type=str, help="Input bases for VACUUM", default='/root/pgsql_script/bases.txt')
parse = parser.parse_args()
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
    try:
        os.system('psql --username="' + username
                  + '" --no-password --dbname="' + str(j)
                  + '"  --command=\"VACUUM (VERBOSE, ANALYZE, FREEZE, FULL);\" ')
        print("Created VACUUM for " + j)
    except FileExistsError as err:
        print(err)