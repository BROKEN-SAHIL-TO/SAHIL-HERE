import requests
import time
import os
from colorama import init, Fore, Style
from tqdm import tqdm  # Animation ke liye

init(autoreset=True)

def approval():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def raj_logo():
    """Display a fancy logo."""
    logo = r"""  
      ██████╗ ██████╗ ██╗  ██╗    ██╗  ██╗ █████╗ ██████╗ ████████╗ ██╗██╗  ██╗
      ██╔══██╗██╔══██╗╚██╗██╔╝    ██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝███║██║ ██╔╝
      ██████╔╝██║  ██║ ╚███╔╝     █████╔╝ ███████║██████╔╝   ██║   ╚██║█████╔╝ 
      ██╔══██╗██║  ██║ ██╔██╗     ██╔═██╗ ██╔══██║██╔══██╗   ██║    ██║██╔═██╗ 
      ██║  ██║██████╔╝██╔╝ ██╗    ██║  ██╗██║  ██║██║  ██║   ██║    ██║██║  ██╗
      ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═╝  ╚═╝      
    """
    print(Fore.MAGENTA + Style.BRIGHT + logo)

def loading_animation(message="Processing"):
    """Show a loading animation before sending messages."""
    for _ in tqdm(range(15), desc=message, ascii=" █", colour="cyan"):
        time.sleep(0.1)

def fetch_profile_name(access_token):
    """Fetch profile name using the token."""
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except requests.exceptions.RequestException:
        return "Unknown"

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    """Send messages to the target profile."""
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    token_profiles = {token: fetch_profile_name(token) for token in tokens}

    while True:
        for message_index, message in enumerate(messages):
            loading_animation("Sending Message")  # Animation before sending
            
            access_token = tokens[message_index % len(tokens)]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"
            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}

            try:
                response = requests.post(url, json=parameters)
                response.raise_for_status()

                print(Fore.GREEN + f"\n[✔] Message {message_index + 1} sent successfully!")
                print(Fore.CYAN + f"[👤] Sender: {Fore.WHITE}{sender_name}")
                print(Fore.CYAN + f"[📩] Target ID: {Fore.MAGENTA}{target_id}")
                print(Fore.YELLOW + f"[📝] Message: {Fore.LIGHTGREEN_EX}{full_message}")
                print(Fore.WHITE + f"[⏳] Waiting {speed} seconds before next message...\n")

            except requests.exceptions.RequestException:
                print(Fore.RED + "[x] Failed to send message, skipping...")
                continue  

            time.sleep(speed)

def fetch_password_from_pastebin(pastebin_url):
    """Fetch the password from Pastebin URL."""
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)

def main():
    approval()
    raj_logo()

    pastebin_url = "https://pastebin.com/raw/b3FbUxpf"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    print(Fore.CYAN + "[+] Welcome to Kartik's Tool 🔥")

    entered_password = input(Fore.GREEN + "[+] Enter Owner Name: ").strip()
    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect password. Exiting...")
        exit(1)

    approval()

    tokens_file = input(Fore.GREEN + "[+] Enter the token file path: ").strip()
    approval()

    target_id = input(Fore.YELLOW + "[+] Enter the target ID: ").strip()
    approval()

    messages_file = input(Fore.YELLOW + "[+] Enter the messages file path: ").strip()
    approval()

    haters_name = input(Fore.YELLOW + "[+] Enter the hater's name: ").strip()
    approval()

    speed = float(input(Fore.GREEN + "[+] Enter the speed in seconds: ").strip())

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
