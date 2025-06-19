import os
import shutil


folder_path = r"C:\Downloads\test\Documents"

categories = {
    "Images": ['.jpg', '.png'],
    "Documents": ['.pdf', '.txt'],
    "Code": ['.py']
}


for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file)

    if os.path.isfile(full_path):
        _, ext = os.path.splitext(file)
        moved = False

        for folder, extensions in categories.items():
            if ext.lower() in extensions:
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(full_path, os.path.join(dest_folder, file))
                print(f"Moved {file} to {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Other")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(other_folder, file))
            print(f"Moved {file} to Other")
