import requests
import time
import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def animate_text(text, delay=0.05):
    """Function to create a typing animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after typing

def approval():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def raj_logo():
    """Display the logo."""
    logo = r"""  
        ██████╗ ██████╗ ██╗  ██╗    ██╗  ██╗ █████╗ ██████╗ ████████╗ ██╗██╗  ██╗ 
        ██╔══██╗██╔══██╗╚██╗██╔╝    ██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝███║██║ ██╔╝ 
        ██████╔╝██║  ██║ ╚███╔╝     █████╔╝ ███████║██████╔╝   ██║   ╚██║█████╔╝  
        ██╔══██╗██║  ██║ ██╔██╗     ██╔═██╗ ██╔══██║██╔══██╗   ██║    ██║██╔═██╗  
        ██║  ██║██████╔╝██╔╝ ██╗    ██║  ██╗██║  ██║██║  ██║   ██║    ██║██║  ██╗ 
        ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═╝  ╚═╝                                                                    
    """
    print(Fore.MAGENTA + Style.BRIGHT + logo)

def fetch_password_from_pastebin(pastebin_url):
    """Fetch the password from the provided Pastebin URL."""
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)  # Exit if the request fails

def main():
    approval()
    raj_logo()

    pastebin_url = "https://pastebin.com/raw/b3FbUxpf"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    # Animated user input prompts
    animate_text(Fore.CYAN + "[+] Welcome to KART1K Tool! Please authenticate.")

    animate_text(Fore.GREEN + "[+] 🎉 Enter Owner Name: ", delay=0.07)
    entered_password = input().strip()

    if entered_password != correct_password:
        animate_text(Fore.RED + "[x] Incorrect password. Exiting program.", delay=0.07)
        exit(1)

    approval()
    
    # Animated Inputs
    animate_text(Fore.GREEN + "[+] Enter the token file: ", delay=0.07)
    tokens_file = input().strip()

    approval()
    
    animate_text(Fore.YELLOW + "[+] Enter the target ID: ", delay=0.07)
    target_id = input().strip()

    approval()

    animate_text(Fore.YELLOW + "[+] Enter the messages file: ", delay=0.07)
    messages_file = input().strip()

    approval()

    animate_text(Fore.YELLOW + "[+] Enter the hater's name: ", delay=0.07)
    haters_name = input().strip()

    approval()

    animate_text(Fore.GREEN + "[+] Enter the speed in seconds: ", delay=0.07)
    speed = float(input().strip())

    approval()

    animate_text(Fore.CYAN + "[+] Processing... Please wait!", delay=0.05)
    time.sleep(2)

    # Call the send_messages function (not included here for brevity)
    # send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
