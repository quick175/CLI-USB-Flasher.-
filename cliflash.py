\
import os 
import tkinter as tk
import time
from tkinter import filedialog
import subprocess
import platform






print("Supported file types ===> .iso,.zip,.img,.bin,")
def flash_L(img_path):
    subprocess.run('lsblk')
    time.sleep(2)
    drive = input("Insert Drive Name (e.g., /dev/sda): ").strip()
    
    if not drive.startswith('/dev/'):
        print("Invalid drive. Must start with /dev")
        return
    
    if not os.path.exists(drive):
        print("Drive not found. Check `lsblk` and try again.")
        subprocess.run('lsblk')
        return
    
    
    confirm = input(f"WARNING: This will ERASE {drive}. Proceed? (y/N): ").lower()
    if confirm != 'y':
        print("Cancelled.")
        return
    
    subprocess.run(f'sudo dd if={img_path} of={drive} bs=4M status=progress && sync', shell=True)




def filetype(filepath):
    filename = filepath.replace('\\', '/').split('/')[-1]
    parts = filename.split('.')
    if '.' not in filename:
        return None    
    if len(parts) > 1:
        return parts[-1].lower()
    return ''
    if ext in ('iso', 'img', 'bin', 'raw'):
        return ext
    elif ext in ('zip', '7z','xz'):
        print("Extracting....")
        subprocess.run(f"7z x '{img_path}'")
    

global img_path
global ext
img_path = tk.filedialog.askopenfilename(title="Select file to flash")
print("Selected file:", img_path)
ext = filetype(img_path)
flash_L(img_path)


