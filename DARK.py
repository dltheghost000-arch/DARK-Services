# DARK.py
import os
import sys

# تعريف الألوان (ANSI escape codes)
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'  # يرجع اللون طبيعي

os.system('clear')

print(f"{PURPLE}welcome to DARK services..!{RESET}")
print(f"{CYAN}services==>channels,websites{RESET}")
print(f"{YELLOW}==>developer,numberbot (NEEDS PERMISSION){RESET}")

name = input(f'{GREEN}CHOOSE YOUR SERVICE: {RESET}')

if name == "websites":
    print(f"{BLUE}GHOST EMPIRE==>https://darklordtheghost.gt.tc{RESET}")

elif name == "files":
    user_name = input(f'{GREEN}user name: {RESET}')
    if user_name == 'DARK':
        password = input(f'{GREEN}password: {RESET}')
        if password == '882012':
            print(f"{GREEN}Access granted..!{RESET}")
            print(f"{BLUE}==>https://t.me/DA4KSOURCE_BOT{RESET}")
        else:
            print(f"{RED}Wrong password!{RESET}")
    else:
        print(f"{RED}Wrong username!{RESET}")

elif name == 'channels':
    print(f"{BLUE}TELEGRAM==>https://t.me/DA4K_HAcK{RESET}")

elif name == "developer":
    print(f"{BLUE}===>https://t.me/GTDERBOT{RESET}")

elif name == "numberbot":
    user_name = input(f'{GREEN}user name: {RESET}')
    if user_name == 'GHOST':
        password = input(f'{GREEN}password: {RESET}')
        if password == '4882012':
            print(f"{GREEN}Access granted..!{RESET}")
            print(f"{BLUE}==> https://t.me/NumberNest_2_Bot{RESET}")
            print(f"{BLUE}==> https://t.me/Number_Nest_Bot{RESET}")
        else:
            print(f"{RED}Wrong password!{RESET}")
    else:
        print(f"{RED}Wrong username!{RESET}")

else:
    print(f"{RED}Invalid service! Please choose from the list.{RESET}")
