import os
import shutil

# List of source directories

from_id = 121
to_id = 130

group = "gh"

source_directories = [f"STT_NS{i:04}" for i in range(from_id, to_id + 1)]

# Target directory
target_directory = f"segments_ns_{group}_{from_id}_{to_id}"

# Ensure target directory exists
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Iterate through source directories
for source_dir in source_directories:
    # Iterate through files in the source directory
    for root, _, files in os.walk(os.path.join("after_split", source_dir)):
        for file in files:
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_directory, file)
            
            # Copy the file to the target directory
            shutil.copy2(source_file_path, target_file_path)
            print(f"Copied '{source_file_path}' to '{target_file_path}'")

print("File copying completed.")
