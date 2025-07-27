import os
import shutil

def organize_files_by_extension(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)
        extension = extension[1:].lower()  # remove the dot and lowercase

        if not extension:
            extension = 'no_extension'

        # Create folder for extension
        extension_folder = os.path.join(folder_path, extension)
        os.makedirs(extension_folder, exist_ok=True)

        # Move the file
        new_path = os.path.join(extension_folder, filename)
        shutil.move(file_path, new_path)
        print(f"Moved: {filename} --> {extension}/")

if __name__ == "__main__":
    folder_to_organize = input("Enter the full path of the folder to organize: ").strip()
    organize_files_by_extension(folder_to_organize)
