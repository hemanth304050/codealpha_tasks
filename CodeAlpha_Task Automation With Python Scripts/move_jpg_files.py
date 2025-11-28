import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Check if source folder exists
    if not os.path.isdir(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    # Create destination folder if it does not exist
    os.makedirs(destination_folder, exist_ok=True)

    files_moved = 0

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        # Check if file ends with .jpg or .jpeg (case-insensitive)
        if filename.lower().endswith((".jpg", ".jpeg")):
            src_path = os.path.join(source_folder, filename)
            dst_path = os.path.join(destination_folder, filename)

            # Move the file
            shutil.move(src_path, dst_path)
            print(f"Moved: {src_path} -> {dst_path}")
            files_moved += 1

    print(f"\nTotal .jpg/.jpeg files moved: {files_moved}")

if __name__ == "__main__":
    print("Move all .jpg files from one folder to another")

    source = input("Enter source folder path: ").strip()
    destination = input("Enter destination folder path: ").strip()

    move_jpg_files(source, destination)
