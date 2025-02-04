import requests
import time
import os
import sys
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.02):
    """Simulate a typing effect for better visual experience."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_logo():
    """Display the animated logo with a typing effect."""
    clear_screen()
    logo = r"""
          ██████╗ ██████╗ ██╗  ██╗    ██╗  ██╗ █████╗ ██████╗ ████████╗ ██╗██╗  ██╗
          ██╔══██╗██╔══██╗╚██╗██╔╝    ██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝███║██║ ██╔╝
          ██████╔╝██║  ██║ ╚███╔╝     █████╔╝ ███████║██████╔╝   ██║   ╚██║█████╔╝
          ██╔══██╗██║  ██║ ██╔██╗     ██╔═██╗ ██╔══██║██╔══██╗   ██║    ██║██╔═██╗
          ██║  ██║██████╔╝██╔╝ ██╗    ██║  ██╗██║  ██║██║  ██║   ██║    ██║██║  ██╗
          ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═╝  ╚═╝      
    """
    typing_effect(Fore.MAGENTA + Style.BRIGHT + logo, 0.002)
    time.sleep(1)

def animated_input(prompt_text):
    """Display animated input prompts with a decorative look."""
    print(Fore.CYAN + "<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")
    typing_effect(Fore.LIGHTYELLOW_EX + prompt_text, 0.03)
    return input(Fore.GREEN + "➜ ")

def fetch_password_from_pastebin(pastebin_url):
    """Fetch the password from the provided Pastebin URL."""
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)  # Exit if the Pastebin request fails

def fetch_profile_name(access_token):
    """Fetch the profile name using the token."""
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except requests.exceptions.RequestException:
        return "Unknown"

def fetch_target_name(target_id, access_token):
    """Fetch the target profile name using the target ID and token."""
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except requests.exceptions.RequestException:
        return "Unknown Target"

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    """Send messages to the target profile."""
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    # Fetch the profile name for each token
    token_profiles = {token: fetch_profile_name(token) for token in tokens}

    # Fetch the target profile name
    target_profile_name = fetch_target_name(target_id, tokens[0])  # Using the first token for the target fetch

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}

            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

                print(Fore.GREEN + f"\n<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>")
                print(Fore.CYAN + f"[🎉] MESSAGE {message_index + 1} SUCCESSFULLY SENT!")
                print(Fore.CYAN + f"[👤] SENDER: {Fore.WHITE}{sender_name}")
                print(Fore.CYAN + f"[📩] TARGET: {Fore.MAGENTA}{target_profile_name} ({target_id})")
                print(Fore.CYAN + f"[📨] MESSAGE: {Fore.LIGHTGREEN_EX}{full_message}")
                print(Fore.CYAN + f"[⏰] TIME: {Fore.LIGHTWHITE_EX}{current_time}")
                print(Fore.GREEN + f"<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>\n")

            except requests.exceptions.RequestException:
                continue  # Ignore error and continue sending next message

            time.sleep(speed)

        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    clear_screen()
    display_logo()

    # Fetch password from Pastebin
    pastebin_url = "https://pastebin.com/raw/b3FbUxpf"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    entered_password = animated_input("ENTER OWNER NAME➜")
    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect password. Exiting program.")
        exit(1)

    clear_screen()
    display_logo()

    tokens_file = animated_input("ENTER TOKEN FILE➜")
    clear_screen()
    display_logo()

    target_id = animated_input("ENTER CONVO UID ➜")
    clear_screen()
    display_logo()

    messages_file = animated_input("ENTER MESSAGE FILE➜")
    clear_screen()
    display_logo()

    haters_name = animated_input("ENTER HATER NAME➜")
    clear_screen()
    display_logo()

    speed = float(animated_input("ENTER DALY/TIME (in seconds) FOR MESSAGES ➜"))

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
