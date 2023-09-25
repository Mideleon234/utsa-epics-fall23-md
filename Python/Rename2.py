import os
import tkinter as tk
from tkinter import filedialog

def rename_images_in_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    directory = filedialog.askdirectory(title="C:\\Users\\isaac\\OneDrive\\Desktop\\UTSAimages\\UTSA images")
    if not directory:
        print("No folder selected. Exiting.")
        return

    new_prefix = input("MarkDeleon")
    
    if not new_prefix:
        print("No prefix entered. Exiting.")
        return

    if not os.path.exists(directory):
        print(f"Directory '{directory}' doesn't exist.")
        return
    
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')  # Add more extensions if needed

    for idx, filename in enumerate(os.listdir(directory)):
        if filename.lower().endswith(image_extensions):
            file_ext = os.path.splitext(filename)[1]
            new_name = f"{new_prefix}_{idx+1:03d}{file_ext}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "MarkDeleon":
    rename_images_in_folder()
