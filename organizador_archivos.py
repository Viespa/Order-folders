import os
import shutil
from pathlib import Path

FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Compresses': ['.zip', '.rar', '.tar'],
    'Others': []
}

def move_file(file, folder_dest):
    Path(folder_dest).mkdir(parents=True, exist_ok=True)  # Create folder if not exists
    try:
        shutil.move(file, folder_dest)
        print(f'Move: {file} -> {folder_dest}')
    except Exception as e:
        print(f'Error to move {file}: {e}')

def order_files(origin_folder):
    for file in os.listdir(origin_folder):
        file_path = os.path.join(origin_folder, file)
        if os.path.isfile(file_path):
            ext = Path(file).suffix.lower()
            move = False
            for file, extensions in FOLDERS.items():
                if ext in extensions:
                    move_file(file_path, os.path.join(origin_folder, file))
                    move = True
                    break
            if not move:
                move_file(file_path, os.path.join(origin_folder, 'Others'))


if __name__ == "__main__":
    origin_folder = input("Enter the path of the folder you want to organize: ")
    order_files(origin_folder)
    print("Organization completed.")
