import subprocess
import os
from colorama import Fore, init

init(autoreset=True)

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

if __name__ == "__main__":
    info_functions = [
        get_baseboard_info, get_mac_address, get_cpu_info,
        get_gpu_info, get_disk_drive_info, get_motherboard_info,
        get_ram_info, get_bios_info, get_smbios_info
    ]

    for info_function in info_functions:
        result = info_function()
        print(result)

    os.system("pause >nul")
