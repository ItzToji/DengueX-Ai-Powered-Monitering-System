"""
FINAL DATASET BALANCING SCRIPT
-----------------------------
Purpose:
- Downsample classes to target size
- Works with your FINAL structure:
    Aedes / Non_Aedes / Unknown

Features:
✔ Uses only image files
✔ Prevents accidental deletion of non-images
✔ Safe to run multiple times
"""

import os
import random

# -------------------------------
# CONFIGURATION
# -------------------------------

BASE = r"F:\Model training\final_dataset"

# Target number of images per class
TARGETS = {
    "Aedes": 5000,
    "Non_Aedes": 5000,
    "Unknown": 5000
}

# Valid image formats
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp")

# -------------------------------
# FUNCTION: DOWNSAMPLE
# -------------------------------

def downsample(folder_path, target_size):
    """
    Reduces number of images in folder to target_size.
    """

    # Get only image files
    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(VALID_EXTENSIONS)
    ]

    print("\n----------------------------------")
    print(f"Processing folder: {folder_path}")
    print(f"Current size: {len(files)}")
    print(f"Target size: {target_size}")

    # If already smaller → do nothing
    if len(files) <= target_size:
        print("No changes needed (already within target)")
        return

    # Shuffle randomly
    random.shuffle(files)

    # Select files to remove
    files_to_remove = files[target_size:]

    removed_count = 0

    for file_name in files_to_remove:
        file_path = os.path.join(folder_path, file_name)

        try:
            os.remove(file_path)
            removed_count += 1
        except Exception as e:
            print(f"Error removing {file_name}: {e}")

    print(f"Removed {removed_count} files")


# -------------------------------
# MAIN
# -------------------------------

if __name__ == "__main__":

    print("Starting dataset balancing...\n")

    for class_name, target_size in TARGETS.items():

        folder_path = os.path.join(BASE, class_name)

        if not os.path.exists(folder_path):
            print(f"WARNING: Folder not found -> {folder_path}")
            continue

        downsample(folder_path, target_size)

    print("\nDataset balancing completed.")