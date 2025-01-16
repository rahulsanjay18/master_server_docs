from tqdm import tqdm
from glob import glob
import os
import shutil

kh_path = '/media/rshah17/Drive 3/Khan_Academy/'

if not os.path.exists(kh_path+'Uncategorized'):
    os.makedirs(kh_path / 'Uncategorized')

uncat_path = kh_path / 'Uncategorized'

for path in glob(kh_path + '*'):
    
    file_name = path.split('/')[-1]
    if '|' in path:

        name_dir = file_name.split('|')[-2].split()
    
        folder_path = kh_path / name_dir

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        shutil.move(path, folder_path / file_name)
    else:
        shutil.move(path, uncat_path / file_name)

