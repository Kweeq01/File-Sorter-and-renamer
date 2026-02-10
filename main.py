import os
from pathlib import Path
from datetime import datetime
import shutil
from collections import defaultdict

path_name = input(r'Введите путь к папке для сортировки: ')

if os.path.exists(path_name):  
    print(f"Папка {path_name} существует. \n")

    folders = {
        '.jpg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.pdf': 'Documents',
        '.txt': 'Documents',
        '.docx': 'Documents'
    }

    counters = defaultdict(lambda:1)

    pathlist = Path(path_name).glob('**/*')

    for file_path in sorted(pathlist):
        if file_path.is_file():
            file_suffix = file_path.suffix.lower()
        
            if file_suffix in folders:
                folder_name = folders[file_suffix]
                dest_folder = os.path.join(path_name, folder_name)

                os.makedirs(dest_folder, exist_ok=True)

                mtime = os.path.getmtime(file_path)
                date_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

                number_str = str(counters[folder_name]).zfill(3)
                counters[folder_name] += 1

                new_name = f"{date_str}_{number_str}{file_suffix}"
                dest_path = os.path.join(dest_folder, new_name)

                shutil.move(str(file_path), dest_path)

                print(f"{file_path} → {dest_path}")
    
else:  
    print(f"Папка {path_name} не существует.")