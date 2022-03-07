# importerede moduler
import os
import shutil
# source mappe
source_dir = '/Users/moa/Documents/backup1'
# destination mappe
dst_dir = '/Users/moa/Documents/backup2'
# lister filer i source mappe
files = os.listdir(source_dir)
# kopier fra source mappe til destination mappe
shutil.copytree(source_dir, dst_dir)

