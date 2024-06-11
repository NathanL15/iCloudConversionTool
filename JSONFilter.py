import os

directory = r'C:\Users\Nathan\Pictures\New folder\Photos-001'

# List all files in the directory
files = os.listdir(directory)

# Filter out files with the .json extension
json_files = [file for file in files if file.endswith('.json')]
heic_files = [file for file in files if file.endswith('.heic')]

# Delete each JSON file
for file in json_files:
    os.remove(os.path.join(directory, file))

# Rename each HEIC file to JPG
for file in heic_files:
    heic_file_path = os.path.join(directory, file)
    jpg_file_path = os.path.join(directory, file.replace('.heic', '.jpg'))
    os.rename(heic_file_path, jpg_file_path)
    
print("Finished")