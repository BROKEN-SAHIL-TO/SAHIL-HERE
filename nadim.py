import requests
import time
import os
import sys
from colorama import init, Fore, Style
from tqdm import tqdm  # Loading Bar Animation
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn
from rich.spinner import Spinner

init(autoreset=True)

console = Console()

def approval():
    """Clear the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

def loading_animation(text="Processing..."):
    """Show a fancy loading animation with tqdm."""
    for _ in tqdm(range(20), desc=Fore.CYAN + text, bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}"):
        time.sleep(0.1)

def raj_logo():
    """Display the logo and add a cool animation effect."""
    approval()
    console.print("\n[bold cyan]⏳ Loading Tool...[/bold cyan]", justify="center")
    time.sleep(1.5)
    
    approval()
    
    logo = r"""
      ██████╗ ██████╗ ██╗  ██╗    ██╗  ██╗ █████╗ ██████╗ ████████╗ ██╗██╗  ██╗
      ██╔══██╗██╔══██╗╚██╗██╔╝    ██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝███║██║ ██╔╝
      ██████╔╝██║  ██║ ╚███╔╝     █████╔╝ ███████║██████╔╝   ██║   ╚██║█████╔╝ 
      ██╔══██╗██║  ██║ ██╔██╗     ██╔═██╗ ██╔══██║██╔══██╗   ██║    ██║██╔═██╗ 
      ██║  ██║██████╔╝██╔╝ ██╗    ██║  ██╗██║  ██║██║  ██║   ██║    ██║██║  ██╗
      ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═╝  ╚═╝                                
    """
    
    console.print("[bold magenta]" + logo + "[/bold magenta]", justify="center")
    console.print("[bold green]🔥 Tool Loaded Successfully! 🔥[/bold green]", justify="center")
    time.sleep(1)

def fetch_password_from_pastebin(pastebin_url):
    """Fetch the password from the provided Pastebin URL."""
    try:
        with console.status("[bold cyan]🔑 Fetching password from Pastebin...[/bold cyan]"):
            time.sleep(2)  # Simulating delay
            response = requests.get(pastebin_url)
            response.raise_for_status()
            return response.text.strip()  # Return the password from the Pastebin link
    except requests.exceptions.RequestException:
        console.print("[bold red]❌ Error Fetching Password! Exiting...[/bold red]")
        exit(1)  # Exit if the pastebin request fails

def main():
    raj_logo()  # Show the logo first

    pastebin_url = "https://pastebin.com/raw/b3FbUxpf"

    loading_animation("🔍 Checking Password...")
    
    # Fetch password from Pastebin
    correct_password = fetch_password_from_pastebin(pastebin_url)

    # Password validation
    entered_password = console.input("[bold green]🔑 ENTER OWNER NAME ===> [/bold green]").strip()
    
    if entered_password != correct_password:
        console.print("[bold red]❌ Incorrect Password! Exiting...[/bold red]")
        exit(1)

    approval()  # Clear screen before starting inputs

    tokens_file = console.input("[bold yellow]📜 ENTER THE TOKEN FILE ===> [/bold yellow]").strip()
    target_id = console.input("[bold yellow]🎯 ENTER THE TARGET ID ===> [/bold yellow]").strip()
    messages_file = console.input("[bold yellow]📩 ENTER THE MESSAGES FILE ===> [/bold yellow]").strip()
    haters_name = console.input("[bold yellow]😡 ENTER THE HATER NAME ===> [/bold yellow]").strip()
    speed = float(console.input("[bold cyan]⏳ ENTER THE SPEED SECOND ===> [/bold cyan]").strip())

    with Progress(SpinnerColumn(), BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task("[bold green]📡 Initializing Message Sending...[/bold green]", total=100)
        for _ in range(100):
            time.sleep(0.02)
            progress.update(task, advance=1)

    console.print("[bold green]✅ Ready to send messages![/bold green]", justify="center")
    
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
