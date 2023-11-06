import os
import sys
import time
from colorama import Fore, Style

temp_directory = "C:\\Windows\\Temp"

def delete_files_in_directory(directory):
    total_files = len(os.listdir(directory))
    if total_files == 0:
        sys.stdout.write(f"\r[{Fore.GREEN}!{Style.RESET_ALL}] No files to delete.  \n")
        print("")
        return

    deleted_files = 0
    start_time = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted_files += 1
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
                deleted_files += 1
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
        progress = (deleted_files / total_files) * 100
        elapsed_time = time.time() - start_time
        remaining_time = 5 - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
        sys.stdout.write(f"\r[{Fore.GREEN}!{Style.RESET_ALL}] Deleting... [{int(progress)}%]  (Time remaining: {remaining_time:.2f}s")
        sys.stdout.flush()
        time.sleep(0.05)

    sys.stdout.write(f"\r[{Fore.GREEN}!{Style.RESET_ALL}] Successfully cleaned your Computer!  \n")

delete_files_in_directory(temp_directory)
