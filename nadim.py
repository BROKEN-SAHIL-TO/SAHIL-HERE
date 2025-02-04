import requests
import time
import os
import sys
from tqdm import tqdm  # Progress Bar Animation
from colorama import init, Fore, Style

init(autoreset=True)

def approval():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_text(text, delay=0.05):
    """Typing effect animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to new line

def loading_animation(message="Loading"):
    """Simple loading animation."""
    for _ in tqdm(range(10), desc=message, ascii=True, bar_format="{l_bar}{bar}"):
        time.sleep(0.2)  # Simulating loading time

def raj_logo():
    """Display logo with animation."""
    logo = r"""  
      ██████╗ ██████╗ ██╗  ██╗    ██╗  ██╗ █████╗ ██████╗ ████████╗ ██╗██╗  ██╗
      ██╔══██╗██╔══██╗╚██╗██╔╝    ██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝███║██║ ██╔╝
      ██████╔╝██║  ██║ ╚███╔╝     █████╔╝ ███████║██████╔╝   ██║   ╚██║█████╔╝ 
      ██╔══██╗██║  ██║ ██╔██╗     ██╔═██╗ ██╔══██║██╔══██╗   ██║    ██║██╔═██╗ 
      ██║  ██║██████╔╝██╔╝ ██╗    ██║  ██╗██║  ██║██║  ██║   ██║    ██║██║  ██╗
      ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═╝  ╚═╝                                                                         
    """
    animated_text(Fore.MAGENTA + Style.BRIGHT + logo, delay=0.002)

def send_message_simulation():
    """Simulated message sending animation."""
    animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%",
                 "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%",
                 "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%",
                 "[■■■■■■■■■■] 100% ✅"]
    
    for frame in animation:
        sys.stdout.write("\r" + Fore.CYAN + frame)
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def send_messages():
    """Fake message sending with animation."""
    approval()
    raj_logo()

    animated_text(Fore.YELLOW + "[+] Initializing message system...", 0.05)
    loading_animation("Setting up")
    
    messages = ["Hello!", "How are you?", "This is an automated message.", "Enjoy coding!"]
    
    for index, message in enumerate(messages):
        print(Fore.GREEN + f"\n[📩] Sending message {index + 1}...")
        send_message_simulation()
        print(Fore.LIGHTBLUE_EX + f"[✔] Message Sent: {message}")
        time.sleep(1)  # Delay between messages
    
    print(Fore.YELLOW + "\n[🎉] All messages sent successfully!\n")

def main():
    approval()
    raj_logo()
    
    animated_text(Fore.CYAN + "[+] Welcome to the Kartik Automated Messaging Tool", 0.04)
    
    approval()
    send_messages()

if __name__ == "__main__":
    main()
