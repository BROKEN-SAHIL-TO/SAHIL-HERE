import requests
import time
import os
from colorama import init, Fore, Style
from tqdm import tqdm  # Progress Bar Animation

init(autoreset=True)

def approval():
    """Clear the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

def loading_animation(text="Processing..."):
    """Show a loading animation"""
    for _ in tqdm(range(10), desc=Fore.CYAN + text, bar_format="{l_bar}{bar}"):
        time.sleep(0.2)

def raj_logo():
    """Display the logo and clear the screen after displaying it."""
    approval()  # Clear screen before showing logo
    loading_animation("Loading Tool...")  # Added Animation
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
        return response.text.strip()  # Return the password from the Pastebin link
    except requests.exceptions.RequestException:
        exit(1)  # Exit if the pastebin request fails

def main():
    raj_logo()  # Show the logo first
    pastebin_url = "https://pastebin.com/raw/b3FbUxpf"  # URL of the pastebin containing the password
    
    loading_animation("Fetching Password...")  # Added Animation
    
    # Fetch password from Pastebin
    correct_password = fetch_password_from_pastebin(pastebin_url)

    # Password validation
    entered_password = input(Fore.GREEN + "[+] 🎉 ENTER OWNER NAME ===>> ").strip()
    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect password. Exiting program.")
        exit(1)  # Exit the program if password is incorrect

    approval()  # Clear screen before starting inputs

    tokens_file = input(Fore.GREEN + "[+] ENTER THE TOKEN FILE ===>> ").strip()
    target_id = input(Fore.YELLOW + "[+] ENTER THE TARGET ID ===>> ").strip()
    messages_file = input(Fore.YELLOW + "[+] ENTER THE MESSAGES FILE ===>> ").strip()
    haters_name = input(Fore.YELLOW + "[+] ENTER THE HATER NAME ===>> ").strip()
    speed = float(input(Fore.GREEN + "[+] ENTER THE SPEED SECOND ===>> ").strip())

    loading_animation("Initializing Message Sending...")  # Added Animation

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
