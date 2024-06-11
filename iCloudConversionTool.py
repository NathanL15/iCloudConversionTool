import os

directory = r'C:\Users\Nathan\Pictures\New folder\Photos-001 (4)'

# List all files in the directory
files = os.listdir(directory)

# Filter out files with the .json extension
json_files = [file for file in files if file.endswith('.json')]
heic_files = [file for file in files if file.endswith('.heic')]
HEIC_files = [file for file in files if file.endswith('.HEIC')]
mov_files = [file for file in files if file.endswith('.mov')]
MOV_files = [file for file in files if file.endswith('.MOV')]
MTS_files = [file for file in files if file.endswith('.MTS')]
i = 1
# Delete each JSON file
for file in json_files:
    os.remove(os.path.join(directory, file))

# Rename each HEIC file to JPG
for file in heic_files:
    heic_file_path = os.path.join(directory, file)
    jpg_file_path = os.path.join(directory, file.replace('.heic', '.jpeg'))
    try:
        os.rename(heic_file_path, jpg_file_path)
    except FileExistsError:
        while True:
            iterate = f"({i})"
            new_heic_file = f"{heic_file_path[:-5]}{iterate}.heic"
            new_jpg_file = f"{jpg_file_path[:-5]}{iterate}.jpeg"
            try:
                os.rename(heic_file_path, new_heic_file)
                heic_file_path = new_heic_file
                jpg_file_path = new_jpg_file
                os.rename(new_heic_file, jpg_file_path)
                break
            except FileExistsError:
                i += 1
    
for file in HEIC_files:
    heic_file_path = os.path.join(directory, file)
    jpg_file_path = os.path.join(directory, file.replace('.HEIC', '.jpeg'))
    try:
        os.rename(heic_file_path, jpg_file_path)
    except FileExistsError:
        while True:
            iterate = f"({i})"
            new_heic_file = f"{heic_file_path[:-5]}{iterate}.HEIC"
            new_jpg_file = f"{jpg_file_path[:-5]}{iterate}.jpeg"
            try:
                os.rename(heic_file_path, new_heic_file)
                heic_file_path = new_heic_file
                jpg_file_path = new_jpg_file
                os.rename(new_heic_file, jpg_file_path)
                break
            except FileExistsError:
                i += 1
        
for file in mov_files:
    mov_file_path = os.path.join(directory, file)
    MP4_file_path = os.path.join(directory, file.replace('.mov', '.MP4'))
    try:
        os.rename(mov_file_path, MP4_file_path)
    except FileExistsError:
        while True:
            iterate = f"({i})"
            new_mov_file = f"{mov_file_path[:-5]}{iterate}.mov"
            new_MP4_file = f"{MP4_file_path[:-5]}{iterate}.mp4"
            try:
                os.rename(mov_file_path, new_mov_file)
                mov_file_path = new_mov_file
                MP4_file_path = new_MP4_file
                os.rename(new_mov_file, MP4_file_path)
                break
            except FileExistsError:
                i += 1
                
for file in MOV_files:
    MOV_file_path = os.path.join(directory, file)
    MP4_file_path = os.path.join(directory, file.replace('.MOV', '.MP4'))
    try:
        os.rename(MOV_file_path, MP4_file_path)
    except FileExistsError:
        while True:
            iterate = f"({i})"
            new_MOV_file = f"{MOV_file_path[:-5]}{iterate}.MOV"
            new_MP4_file = f"{MP4_file_path[:-5]}{iterate}.mp4"
            try:
                os.rename(MOV_file_path, new_MOV_file)
                MOV_file_path = new_MOV_file
                MP4_file_path = new_MP4_file
                os.rename(new_MOV_file, MP4_file_path)
                break
            except FileExistsError:
                i += 1
                
for file in MTS_files:
    MTS_file_path = os.path.join(directory, file)
    MP4_file_path = os.path.join(directory, file.replace('.MTS', '.MP4'))
    try:
        os.rename(MTS_file_path, MP4_file_path)
    except FileExistsError:
        while True:
            iterate = f"({i})"
            new_MTS_file = f"{MTS_file_path[:-5]}{iterate}.MTS"
            new_MP4_file = f"{MP4_file_path[:-5]}{iterate}.mp4"
            try:
                os.rename(MTS_file_path, new_MTS_file)
                MTS_file_path = new_MTS_file
                MP4_file_path = new_MP4_file
                os.rename(new_MTS_file, MP4_file_path)
                break
            except FileExistsError:
                i += 1
        
print("Finished")