import time
import sys
import os
from colorama import Fore, Style, init

init()

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
            os.system('python checker.py')
            input("Enter to Exit")
        elif choice == "2":
            clear_terminal()
            os.system('python cleaner.py')
            input("Enter to Exit")
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Invalid Option...")

if __name__ == "__main__":
    main()
