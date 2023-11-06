import os
import sys
import time
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

temp_directory = "C:\\Windows\\Temp"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_loading_bar():
    total_time = 15
    step_time = total_time / 100

    for i in range(101):
        sys.stdout.write(f'\r[{Fore.GREEN}{"#" * i}{Style.RESET_ALL}{" " * (100 - i)}] {i}%')
        sys.stdout.flush()
        time.sleep(step_time)
    sys.stdout.write(f"\n\n[{Fore.GREEN}!{Style.RESET_ALL}] Successfully Spoofed your Computer!\n")
    sys.stdout.flush()

def spoof_computer():
    clear_terminal()
    print("Spoofing...")
    print("")
    print_loading_bar()
    print("")
    input("Press Enter to Exit...")

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

    sys.stdout.write(f"\r[{Fore.GREEN}!{Style.RESET_ALL}] Successfully cleaned your Computer!\n\n")

def get_baseboard_info():
    try:
        baseboard_serial = subprocess.check_output("wmic baseboard get serialnumber").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} Baseboard\n{baseboard_serial}\n"
    except Exception as e:
        return f"Error retrieving baseboard information: {str(e)}"

def get_mac_address():
    try:
        mac_address = subprocess.check_output("""wmic path Win32_NetworkAdapter where "PNPDeviceID like '%%PCI%%' AND NetConnectionStatus=2 AND AdapterTypeID='0'" get MacAddress""").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} Mac\n{mac_address}\n"
    except Exception as e:
        return f"Error retrieving MAC address: {str(e)}"

def get_cpu_info():
    try:
        cpu_id = subprocess.check_output("wmic cpu get processorid").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} CPU\n{cpu_id}\n"
    except Exception as e:
        return f"Error retrieving CPU information: {str(e)}"

def get_gpu_info():
    try:
        gpu_info = subprocess.check_output("wmic PATH Win32_VideoController GET Description,PNPDeviceID").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} GPU\n{gpu_info}\n"
    except Exception as e:
        return f"Error retrieving GPU information: {str(e)}"

def get_disk_drive_info():
    try:
        disk_serial = subprocess.check_output("wmic diskdrive get serialnumber").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} DISK DRIVE\n{disk_serial}\n"
    except Exception as e:
        return f"Error retrieving disk drive information: {str(e)}"

def get_motherboard_info():
    try:
        motherboard_serial = subprocess.check_output("wmic baseboard get serialnumber").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} MotherBoard\n{motherboard_serial}\n"
    except Exception as e:
        return f"Error retrieving motherboard information: {str(e)}"

def get_ram_info():
    try:
        ram_serial = subprocess.check_output("wmic memorychip get serialnumber").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} RAM\n{ram_serial}\n"
    except Exception as e:
        return f"Error retrieving RAM information: {str(e)}"

def get_bios_info():
    try:
        bios_serial = subprocess.check_output("wmic bios get serialnumber").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} Bios\n{bios_serial}\n"
    except Exception as e:
        return f"Error retrieving BIOS information: {str(e)}"

def get_smbios_info():
    try:
        smbios_uuid = subprocess.check_output("wmic csproduct get uuid").decode().strip()
        return f"{Fore.GREEN}[</>]{Fore.RESET} smBios\n{smbios_uuid}\n"
    except Exception as e:
        return f"Error retrieving smBios information: {str(e)}"

def main():
    while True:
        clear_terminal()
        print(f"[{Fore.GREEN}1{Fore.RESET}] Spoof")
        print(f"[{Fore.GREEN}2{Fore.RESET}] Cleaner")
        print(f"[{Fore.GREEN}3{Fore.RESET}] Checker")
        print(f"[{Fore.GREEN}4{Fore.RESET}] Exit")
        print("")
        choice = input("Select Option: ")

        if choice == "1":
            spoof_computer()
        elif choice == "4":
            clear_terminal()
            break
        elif choice == "3":
            clear_terminal()
            info_functions = [
                get_baseboard_info, get_mac_address, get_cpu_info,
                get_gpu_info, get_disk_drive_info, get_motherboard_info,
                get_ram_info, get_bios_info, get_smbios_info
            ]

            for info_function in info_functions:
                result = info_function()
                print(result)
            input("Press Enter to Exit...")
        elif choice == "2":
            clear_terminal()
            delete_files_in_directory(temp_directory)
            input("Press Enter to Exit...")
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Invalid Option...")

if __name__ == "__main__":
    main()
