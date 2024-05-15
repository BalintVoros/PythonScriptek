
import os
import shutil

def organize_files_by_category(directory):
    # Mapping of file extensions to more specific folder names
    extensions_map = {
        'Documents': ['docx'],
        'PDF': ['pdf'],
        'Codes': ['py', 'js', 'java', 'c', 'cpp', 'cs', 'h'],
        'Pictures': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        'Archives': ['zip', 'rar', '7z', 'tar', 'gz'],
        'Torrents': ['torrent'],
        'Videos': ['mp4', 'avi', 'mkv', 'mov', 'flv', 'wmv'],
        'Movies': ['mp4', 'avi', 'mkv'],
        'Installers': ['exe', 'msi', 'dmg', 'pkg']  # Added for Windows and Mac installers
    }
    
    # Create directories if they do not exist and organize files
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):  # Check if it's a file and not a directory
            filename, file_extension = os.path.splitext(item)
            file_extension = file_extension[1:].lower()  # Remove the dot from the extension and convert to lowercase
            moved = False

            for folder, extensions in extensions_map.items():
                if file_extension in extensions:
                    new_dir = os.path.join(directory, folder)
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)
                    shutil.move(full_path, os.path.join(new_dir, item))
                    moved = True
                    break  # Once moved, no need to check other folders

            # Move unclassified files to 'Other' folder
            if not moved:
                other_dir = os.path.join(directory, 'Other')
                if not os.path.exists(other_dir):
                    os.makedirs(other_dir)
                shutil.move(full_path, os.path.join(other_dir, item))

# Example usage
organize_files_by_category('/home/balint/Letöltések/')
