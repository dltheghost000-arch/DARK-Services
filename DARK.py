#!/usr/bin/env python3
# DARK.py - DARKLORD SERVICES TOOL
import os
import sys

# ==================== الألوان ====================
R = '\033[91m'   # RED
G = '\033[92m'   # GREEN
Y = '\033[93m'   # YELLOW
B = '\033[94m'   # BLUE
P = '\033[95m'   # PURPLE
C = '\033[96m'   # CYAN
W = '\033[97m'   # WHITE
BOLD = '\033[1m'  # BOLD
RE = '\033[0m'   # RESET

# ==================== لوجو DARKLORD رفيع وملون ====================
def show_logo():
    os.system('clear')
    print(f"""
{R}╔══════════════════════════════════════════════════════════════════════════╗{RE}
{R}║{RE}                                                                          {R}║{RE}
{R}║{RE}    {C}DDDD   {Y}AAAA   {G}RRRR   {B}KKKK   {P}L      {C}OOO    {Y}RRRR   {G}DDDD{RE}                                     {R}║{RE}
{R}║{RE}    {C}D   D {Y}A   A  {G}R   R  {B}K   K  {P}L     {C}O   O  {Y}R   R  {G}D   D{RE}                                    {R}║{RE}
{R}║{RE}    {C}D   D {Y}AAAAA  {G}RRRR   {B}KKK    {P}L     {C}O   O  {Y}RRRR   {G}D   D{RE}                                    {R}║{RE}
{R}║{RE}    {C}D   D {Y}A   A  {G}R R    {B}K   K  {P}L     {C}O   O  {Y}R R    {G}D   D{RE}                                    {R}║{RE}
{R}║{RE}    {C}DDDD  {Y}A   A  {G}R  R   {B}K   K  {P}LLLLL {C} OOO   {Y}R  R   {G}DDDD{RE}                                     {R}║{RE}
{R}║{RE}                                                                          {R}║{RE}
{R}║{RE}              {W}{BOLD}DARKLORD SERVICES - ELITE TOOL{RE}                         {R}║{RE}
{R}║{RE}                  {Y}{BOLD}Version 2.0 | BY DARKLORD{RE}                           {R}║{RE}
{R}║{RE}                                                                          {R}║{RE}
{R}╚══════════════════════════════════════════════════════════════════════════╝{RE}
    """)

# ==================== قائمة الخدمات ====================
def show_menu():
    print(f"""
{C}┌─────────────────────────────────────────────────┐{RE}
{C}│{RE}                  {W}{BOLD}AVAILABLE SERVICES{RE}                  {C}│{RE}
{C}├─────────────────────────────────────────────────┤{RE}
{C}│{RE}   {G}1.{RE} websites                                     {C}│{RE}
{C}│{RE}   {G}2.{RE} files {Y}(NEEDS PERMISSION){RE}                       {C}│{RE}
{C}│{RE}   {G}3.{RE} channels                                    {C}│{RE}
{C}│{RE}   {G}4.{RE} developer                                   {C}│{RE}
{C}│{RE}   {G}5.{RE} numberbot {Y}(NEEDS PERMISSION){RE}                     {C}│{RE}
{C}└─────────────────────────────────────────────────┘{RE}

{Y}💡 TIP:{RE} {W}Type {G}'exit'{W} or {G}'quit'{W} to leave DARKLORD Services{RE}
{C}───────────────────────────────────────────────────{RE}
    """)

# ==================== البرنامج الرئيسي ====================
def main():
    while True:
        show_logo()
        show_menu()
        
        service = input(f"{G}🎯 DARKLORD@SERVICE:~# {RE}").lower().strip()
        
        # خروج من البرنامج
        if service in ["exit", "quit", "logout"]:
            print(f"""
{R}╔════════════════════════════════════════════════════╗{RE}
{R}║{RE}    {Y}👋 Exiting DARKLORD Services... Goodbye! 👋{RE}    {R}║{RE}
{R}╚════════════════════════════════════════════════════╝{RE}
            """)
            sys.exit(0)
        
        # ========== الخدمات ==========
        
        # خدمة websites
        if service in ["websites", "1"]:
            print(f"""
{G}╔════════════════════════════════════════════════════╗{RE}
{G}║{RE}   {C}🌐 GHOST EMPIRE{RE}                                  {G}║{RE}
{G}║{RE}   {C}🔗 https://darklordtheghost.gt.tc{RE}               {G}║{RE}
{G}╚════════════════════════════════════════════════════╝{RE}
            """)
        
        # خدمة files
        elif service in ["files", "2"]:
            print(f"""
{B}╔════════════════════════════════════════════════════╗{RE}
            """)
            username = input(f"{W}👤 USERNAME: {RE}")
            if username == 'DARK':
                password = input(f"{W}🔑 PASSWORD: {RE}")
                if password == '882012':
                    print(f"""
{B}║{RE}   {G}✅ Access granted..!{RE}                           {B}║{RE}
{B}║{RE}   {C}🔗 https://t.me/DA4KSOURCE_BOT{RE}                {B}║{RE}
{B}╚════════════════════════════════════════════════════╝{RE}
                    """)
                else:
                    print(f"""
{B}║{RE}   {R}❌ Wrong password!{RE}                             {B}║{RE}
{B}╚════════════════════════════════════════════════════╝{RE}
                    """)
            else:
                print(f"""
{B}║{RE}   {R}❌ Wrong username!{RE}                             {B}║{RE}
{B}╚════════════════════════════════════════════════════╝{RE}
                    """)
        
        # خدمة channels
        elif service in ["channels", "3"]:
            print(f"""
{P}╔════════════════════════════════════════════════════╗{RE}
{P}║{RE}   {C}📢 TELEGRAM CHANNEL{RE}                              {P}║{RE}
{P}║{RE}   {C}🔗 https://t.me/DA4K_HAcK{RE}                      {P}║{RE}
{P}╚════════════════════════════════════════════════════╝{RE}
            """)
        
        # خدمة developer
        elif service in ["developer", "4"]:
            print(f"""
{Y}╔════════════════════════════════════════════════════╗{RE}
{Y}║{RE}   {C}👨‍💻 DEVELOPER CONTACT{RE}                           {Y}║{RE}
{Y}║{RE}   {C}🔗 https://t.me/GTDERBOT{RE}                       {Y}║{RE}
{Y}╚════════════════════════════════════════════════════╝{RE}
            """)
        
        # خدمة numberbot
        elif service in ["numberbot", "5"]:
            print(f"""
{C}╔════════════════════════════════════════════════════╗{RE}
            """)
            username = input(f"{W}👤 USERNAME: {RE}")
            if username == 'GHOST':
                password = input(f"{W}🔑 PASSWORD: {RE}")
                if password == '4882012':
                    print(f"""
{C}║{RE}   {G}✅ Access granted..!{RE}                           {C}║{RE}
{C}║{RE}   {C}🔗 https://t.me/NumberNest_2_Bot{RE}              {C}║{RE}
{C}║{RE}   {C}🔗 https://t.me/Number_Nest_Bot{RE}               {C}║{RE}
{C}╚════════════════════════════════════════════════════╝{RE}
                    """)
                else:
                    print(f"""
{C}║{RE}   {R}❌ Wrong password!{RE}                             {C}║{RE}
{C}╚════════════════════════════════════════════════════╝{RE}
                    """)
            else:
                print(f"""
{C}║{RE}   {R}❌ Wrong username!{RE}                             {C}║{RE}
{C}╚════════════════════════════════════════════════════╝{RE}
                    """)
        
        # خدمة غير صحيحة
        else:
            print(f"""
{R}╔════════════════════════════════════════════════════╗{RE}
{R}║{RE}   {R}❌ Invalid service! Please choose from the list{RE}    {R}║{RE}
{R}║{RE}   {Y}💡 Type {G}'exit'{Y} to quit{RE}                         {R}║{RE}
{R}╚════════════════════════════════════════════════════╝{RE}
            """)
        
        # انتظار قبل الرجوع للقائمة
        print(f"\n{C}───────────────────────────────────────────────────{RE}")
        input(f"{W}⏎ Press Enter to continue...{RE}")

# ==================== تشغيل البرنامج ====================
if __name__ == "__main__":
    main()
