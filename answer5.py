'''Q5. Duplicate File Finder and Cleaner
Write a Python script to find duplicate files within a specified directory and its subdirectories. The script should:
Scan the directory for all files and calculate a checksum (e.g., sha256sum) for each file.
Identify and list duplicate files by comparing their checksums.
Optionally, give the user the option to delete or move duplicate files.
Bonus:
Allow the user to specify the minimum file size for duplication detection (e.g., only consider files larger than 1MB).
Create a report listing the duplicate files and their checksums.
'''
import os
import hashlib
from collections import defaultdict

def get_file_checksum(file_path):
    with open(file_path, "rb") as f:
        checksum = hashlib.sha256()
        while chunk := f.read(4096):
            checksum.update(chunk)
    return checksum.hexdigest()

def find_duplicate_files(directory, min_size=0):
    file_sizes = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) >= min_size:
                file_sizes[os.path.getsize(file_path)].append(file_path)
    
    duplicate_files = []
    for size, files in file_sizes.items():
        if len(files) > 1:
            for file in files:
                checksum = get_file_checksum(file)
                duplicate_files.append((file, checksum))
    
    return duplicate_files

def delete_duplicate_files(duplicate_files):
    for file, _ in duplicate_files:
        os.remove(file)
        print(f"Deleted: {file}")

directory = input("Enter directory path: ")
min_size = int(input("Enter minimum file size (bytes): "))
duplicate_files = find_duplicate_files(directory, min_size)
if duplicate_files:
    print("Duplicate files:")
    for file, checksum in duplicate_files:
        print(f"{file} - {checksum}")
    delete = input("Delete duplicate files? (y/n): ")
    if delete.lower() == "y":
        delete_duplicate_files(duplicate_files)