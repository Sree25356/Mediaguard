# mediaguard_cli.py

import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from mediaguard import (
    check_hash,
    check_metadata,
    detect_faces,
    error_level_analysis,
    detect_ai_generation,
    save_report
)

console = Console()

def banner():
    os.system("clear")
    title = Text("""
███╗   ███╗███████╗██████╗ ██╗ █████╗  ██████╗ █████╗ ██╗   ██╗██████╗ 
████╗ ████║██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██║   ██║██╔══██╗
██╔████╔██║█████╗  ██████╔╝██║███████║██║     ███████║██║   ██║██████╔╝
██║╚██╔╝██║██╔══╝  ██╔═══╝ ██║██╔══██║██║     ██╔══██║██║   ██║██╔═══╝ 
██║ ╚═╝ ██║███████╗██║     ██║██║  ██║╚██████╗██║  ██║╚██████╔╝██║     
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
""", style="bold red")
    console.print(title)
    console.print(Panel("Terminal Interface by [bold yellow]SV 🕶️[/] | [cyan]Media Forensic Toolkit[/]", expand=False))

def main_menu():
    while True:
        banner()
        console.print("\n[bold cyan]Choose an option:[/]")
        console.print(" [1] 🔍 Check Image Hash")
        console.print(" [2] 🧾 Check Image Metadata")
        console.print(" [3] 🧠 Detect Faces in Image")
        console.print(" [4] 🧪 Error Level Analysis (ELA)")
        console.print(" [5] 🤖 AI-Generated Image Detection")
        console.print(" [6] 🚪 Exit")

        choice = input("\n[>] Your choice: ")

        if choice == "1":
            path = input("📂 Image path: ")
            check_hash(path)
        elif choice == "2":
            path = input("📂 Image path: ")
            check_metadata(path)
        elif choice == "3":
            path = input("📂 Image path: ")
            detect_faces(path)
        elif choice == "4":
            path = input("📂 Image path: ")
            error_level_analysis(path)
        elif choice == "5":
            path = input("📂 Image path: ")
            detect_ai_generation(path)
        elif choice == "6":
            console.print("\n[green]✔ Exiting MediaGuard. Stay sharp, SV 🕶️[/green]")
            break
        else:
            console.print("[red]✖ Invalid choice. Try again.[/red]")

        input("\n[↩] Press Enter to return to main menu...")

if __name__ == "__main__":
    main_menu()
