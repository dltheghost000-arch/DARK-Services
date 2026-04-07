#!/usr/bin/env python3
# DARK.py - DARKLORD SERVICES TOOL
import os
import sys

# ==================== الألوان ====================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'

# ==================== لوجو DARKLORD ملون ====================
def show_logo():
    os.system('clear')
    logo = f"""
{RED}{BOLD}╔══════════════════════════════════════════════════════════════════════════╗{RESET}
{RED}{BOLD}║{RESET}                                                                          {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}    {CYAN}██████╗  █████╗ ██████╗ ██╗  ██╗██╗      ██████╗ ██████╗ ██████╗ {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}    {CYAN}██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗{RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}    {CYAN}██║  ██║███████║██████╔╝█████╔╝ ██║     ██║   ██║██████╔╝██║  ██║{RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}    {CYAN}██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║     ██║   ██║██╔══██╗██║  ██║{RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}    {CYAN}██████╔╝██║  ██║██║  ██║██║  ██╗███████╗╚██████╔╝██║  ██║██████╔╝{RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}    {CYAN}╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}                                                                          {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}        {YELLOW}{BOLD}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{RESET}        {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}        {YELLOW}{BOLD}▓{RESET}      {GREEN}{BOLD}DARKLORD SERVICES - ELITE TOOL{RESET}      {YELLOW}{BOLD}▓{RESET}        {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}        {YELLOW}{BOLD}▓{RESET}            {PURPLE}{BOLD}Version 2.0 | BY DARKLORD{RESET}           {YELLOW}{BOLD}▓{RESET}        {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}        {YELLOW}{BOLD}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{RESET}        {RED}{BOLD}║{RESET}
{RED}{BOLD}║{RESET}                                                                          {RED}{BOLD}║{RESET}
{RED}{BOLD}╚══════════════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(logo)

# ==================== قائمة الخدمات ====================
def show_menu():
    print(f"\n{WHITE}{BOLD}┌─────────────────────────────────────────────────┐{RESET}")
    print(f"{WHITE}{BOLD}│{RESET}  {GREEN}{BOLD}📌 AVAILABLE SERVICES{RESET}                            {WHITE}{BOLD}│{RESET}")
    print(f"{WHITE}{BOLD}├─────────────────────────────────────────────────┤{RESET}")
    print(f"{WHITE}{BOLD}│{RESET}  {CYAN}1️⃣  websites{RESET}                                      {WHITE}{BOLD}│{RESET}")
    print(f"{WHITE}{BOLD}│{RESET}  {CYAN}2️⃣  files {DIM}(NEEDS PERMISSION){RESET}                         {WHITE}{BOLD}│{RESET}")
    print(f"{WHITE}{BOLD}│{RESET}  {CYAN}3️⃣  channels{RESET}                                    {WHITE}{BOLD}│{RESET}")
    print(f"{WHITE}{BOLD}│{RESET}  {CYAN}4️⃣  developer{RESET}                                   {WHITE}{BOLD}│{RESET}")
    print(f"{WHITE}{BOLD}│{RESET}  {CYAN}5️⃣  numberbot {DIM}(NEEDS PERMISSION){RESET}                       {WHITE}{BOLD}│{RESET}")
    print(f"{WHITE}{BOLD}└─────────────────────────────────────────────────┘{RESET}")
    print(f"\n{YELLOW}{BOLD}💡 TIP:{RESET} {WHITE}Type {GREEN}'exit'{WHITE} or {GREEN}'quit'{WHITE} to leave DARKLORD Services{RESET}")
    print(f"{DIM}{'─'*59}{RESET}")

# ==================== البرنامج الرئيسي ====================
def main():
    while True:
        show_logo()
        show_menu()
        
        service = input(f"\n{BOLD}{CYAN}🎯 DARKLORD@SERVICE:~#{RESET} ").lower().strip()
        
        # خروج
        if service in ["exit", "quit", "logout"]:
            print(f"\n{RED}{BOLD}╔════════════════════════════════════════════════════╗{RESET}")
            print(f"{RED}{BOLD}║{RESET}      {YELLOW}👋 Exiting DARKLORD Services... Goodbye! 👋{RESET}      {RED}{BOLD}║{RESET}")
            print(f"{RED}{BOLD}╚════════════════════════════════════════════════════╝{RESET}\n")
            sys.exit(0)
        
        # ========== الخدمات ==========
        
        # خدمة websites
        if service in ["websites", "1", "1️⃣"]:
            print(f"\n{GREEN}{BOLD}╔════════════════════════════════════════════════════╗{RESET}")
            print(f"{GREEN}{BOLD}║{RESET}  {WHITE}🌐 GHOST EMPIRE{RESET}                                    {GREEN}{BOLD}║{RESET}")
            print(f"{GREEN}{BOLD}║{RESET}  {CYAN}🔗 https://darklordtheghost.gt.tc{RESET}                     {GREEN}{BOLD}║{RESET}")
            print(f"{GREEN}{BOLD}╚════════════════════════════════════════════════════╝{RESET}")
        
        # خدمة files
        elif service in ["files", "2", "2️⃣"]:
            print(f"\n{BLUE}{BOLD}╔════════════════════════════════════════════════════╗{RESET}")
            username = input(f"{BLUE}{BOLD}║{RESET}  {WHITE}👤 USERNAME:{RESET} ")
            if username == 'DARK':
                password = input(f"{BLUE}{BOLD}║{RESET}  {WHITE}🔑 PASSWORD:{RESET} ")
                if password == '882012':
                    print(f"{BLUE}{BOLD}║{RESET}  {GREEN}✅ Access granted..!{RESET}                        {BLUE}{BOLD}║{RESET}")
                    print(f"{BLUE}{BOLD}║{RESET}  {CYAN}🔗 https://t.me/DA4KSOURCE_BOT{RESET}               {BLUE}{BOLD}║{RESET}")
                else:
                    print(f"{BLUE}{BOLD}║{RESET}  {RED}❌ Wrong password!{RESET}                           {BLUE}{BOLD}║{RESET}")
            else:
                print(f"{BLUE}{BOLD}║{RESET}  {RED}❌ Wrong username!{RESET}                           {BLUE}{BOLD}║{RESET}")
            print(f"{BLUE}{BOLD}╚════════════════════════════════════════════════════╝{RESET}")
        
        # خدمة channels
        elif service in ["channels", "3", "3️⃣"]:
            print(f"\n{PURPLE}{BOLD}╔════════════════════════════════════════════════════╗{RESET}")
            print(f"{PURPLE}{BOLD}║{RESET}  {WHITE}📢 TELEGRAM CHANNEL{RESET}                            {PURPLE}{BOLD}║{RESET}")
            print(f"{PURPLE}{BOLD}║{RESET}  {CYAN}🔗 https://t.me/DA4K_HAcK{RESET}                        {PURPLE}{BOLD}║{RESET}")
            print(f"{PURPLE}{BOLD}╚════════════════════════════════════════════════════╝{RESET}")
        
        # خدمة developer
        elif service in ["developer", "4", "4️⃣"]:
            print(f"\n{YELLOW}{BOLD}╔════════════════════════════════════════════════════╗{RESET}")
            print(f"{YELLOW}{BOLD}║{RESET}  {WHITE}👨‍💻 DEVELOPER CONTACT{RESET}                           {YELLOW}{BOLD}║{RESET}")
            print(f"{YELLOW}{BOLD}║{RESET}  {CYAN}🔗 https://t.me/GTDERBOT{RESET}                         {YELLOW}{BOLD}║{RESET}")
            print(f"{YELLOW}{BOLD}╚════════════════════════════════════════════════════╝{RESET}")
        
        # خدمة numberbot
        elif service in ["numberbot", "5", "5️⃣"]:
            print(f"\n{CYAN}{BOLD}╔════════════════════════════════════════════════════╗{RESET}")
            username = input(f"{CYAN}{BOLD}║{RESET}  {WHITE}👤 USERNAME:{RESET} ")
            if username == 'GHOST':
                password = input(f"{CYAN}{BOLD}║{RESET}  {WHITE}🔑 PASSWORD:{RESET} ")
                if password == '4882012':
                    print(f"{CYAN}{BOLD}║{RESET}  {GREEN}✅ Access granted..!{RESET}                        {CYAN}{BOLD}║{RESET}")
                    print(f"{CYAN}{BOLD}║{RESET}  {CYAN}🔗 https://t.me/NumberNest_2_Bot{RESET}             {CYAN}{BOLD}║{RESET}")
                    print(f"{CYAN}{BOLD}║{RESET}  {CYAN}🔗 https://t.me/Number_Nest_Bot{RESET}             {CYAN}{BOLD}║{RESET}")
                else:
                    print(f"{CYAN}{BOLD}║{RESET}  {RED}❌ Wrong password!{RESET}                           {CYAN}{BOLD}║{RESET}")
            else:
                print(f"{CYAN}{BOLD}║{RESET}  {RED}❌ Wrong username!{RESET}                           {CYAN}{BOLD}║{RESET}")
            print(f"{CYAN}{BOLD}╚════════════════════════════════════════════════════╝{RESET}")
        
        # خدمة غير صحيحة
        else:
            print(f"\n{RED}{BOLD}╔════════════════════════════════════════════════════╗{RESET}")
            print(f"{RED}{BOLD}║{RESET}  {RED}❌ Invalid service! Please choose from the list{RESET}    {RED}{BOLD}║{RESET}")
            print(f"{RED}{BOLD}║{RESET}  {YELLOW}💡 Type {GREEN}'exit'{YELLOW} to quit{RESET}                         {RED}{BOLD}║{RESET}")
            print(f"{RED}{BOLD}╚════════════════════════════════════════════════════╝{RESET}")
        
        # انتظار قبل الرجوع للقائمة
        print(f"\n{DIM}{'─'*59}{RESET}")
        input(f"{WHITE}⏎ Press Enter to continue...{RESET}")

# ==================== تشغيل البرنامج ====================
if __name__ == "__main__":
    main()
