# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import asyncio
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
import argparse
from dotenv import load_dotenv
import os

console = Console()
load_dotenv()

class TOSINT:
    def __init__(self):
        self.version = "0.1"
        self.author = "Emox"
    
    def banner(self):
        console.print(f"""
[bold red]████████╗ ██████╗ ███████╗██╗███╗   ██╗████████╗[/bold red]
[bold red]╚══██╔══╝██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝[/bold red]
[bold red]   ██║   ██║   ██║███████╗██║██╔██╗ ██║   ██║   [/bold red]
[bold red]   ██║   ██║   ██║╚════██║██║██║╚██╗██║   ██║   [/bold red]
[bold red]   ██║   ╚██████╔╝███████║██║██║ ╚████║   ██║   [/bold red]
[bold yellow]   v{self.version} - X/Twitter OSINT Tool by Emox[/bold yellow]
        """, style="bold")

    async def user_info(self, username):
        console.print(f"[bold cyan][*] {username} kullanıcısı araştırılıyor...[/bold cyan]")
        
        # Gerçek veri için twscrape kullanılacak
        data = {
            "username": username,
            "fullname": "API ile çekilecek",
            "followers": "N/A",
            "following": "N/A",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "bio": "Bilgi yok",
            "location": "Bilinmiyor",
            "verified": False
        }
        
        table = Table(title=f"{username} Bilgileri")
        table.add_column("Alan", style="cyan")
        table.add_column("Değer", style="yellow")
        
        for key, value in data.items():
            table.add_row(key.capitalize(), str(value))
        
        console.print(table)
        
        with open(f"{username}_info.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        console.print(f"[green][+] Bilgiler {username}_info.json olarak kaydedildi![/green]")

async def main():
    parser = argparse.ArgumentParser(description="t-osint - X OSINT Aracı")
    parser.add_argument("-u", "--user", help="Hedef X kullanıcı adı")
    parser.add_argument("-v", "--version", action="store_true")
    
    args = parser.parse_args()
    
    tool = TOSINT()
    tool.banner()
    
    if args.version:
        console.print(f"[bold]t-osint v{tool.version}[/bold]")
        return
    
    if args.user:
        await tool.user_info(args.user)
    else:
        console.print("[red]Kullanım: python t_osint.py -u kullanıcıadı[/red]")

if __name__ == "__main__":
    asyncio.run(main())
