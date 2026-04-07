# DARK.py
import os
import sys

def show_logo():
    os.system('clear')
    logo = f"""
{'='*55}
   ██████╗  █████╗ ██████╗ ██╗  ██╗██╗      ██████╗ ██████╗ ██████╗ 
   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗
   ██║  ██║███████║██████╔╝█████╔╝ ██║     ██║   ██║██████╔╝██║  ██║
   ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║     ██║   ██║██╔══██╗██║  ██║
   ██████╔╝██║  ██║██║  ██║██║  ██╗███████╗╚██████╔╝██║  ██║██████╔╝
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
{'='*55}
              🔥 DARKLORD SERVICES - ELITE TOOL 🔥
{'='*55}
"""
    print(logo)

def show_menu():
    print("\n📌 AVAILABLE SERVICES:")
    print("  ┌─────────────────────────────────┐")
    print("  │ 1️⃣  websites                    │")
    print("  │ 2️⃣  files (NEEDS PERMISSION)    │")
    print("  │ 3️⃣  channels                    │")
    print("  │ 4️⃣  developer                   │")
    print("  │ 5️⃣  numberbot (NEEDS PERMISSION)│")
    print("  └─────────────────────────────────┘")
    print("\n💡 TIP: Type 'exit' or 'quit' to leave DARKLORD Services")
    print("-" * 55)

def main():
    while True:
        show_logo()
        show_menu()
        
        name = input("🎯 DARKLORD@SERVICE:~# ").lower().strip()
        
        # خروج من البرنامج
        if name in ["exit", "quit", "logout"]:
            print("\n" + "="*55)
            print("   👋 Exiting DARKLORD Services... Goodbye! 👋")
            print("="*55 + "\n")
            sys.exit(0)
        
        # الخدمات
        if name == "websites" or name == "1" or name == "1️⃣":
            print("\n" + "="*55)
            print("   🌐 GHOST EMPIRE")
            print("   🔗 https://darklordtheghost.gt.tc")
            print("="*55)
        
        elif name == "files" or name == "2" or name == "2️⃣":
            print("\n" + "="*55)
            username = input("   👤 USERNAME: ")
            if username == 'DARK':
                password = input("   🔑 PASSWORD: ")
                if password == '882012':
                    print("   ✅ Access granted..!")
                    print("   🔗 https://t.me/DA4KSOURCE_BOT")
                else:
                    print("   ❌ Wrong password!")
            else:
                print("   ❌ Wrong username!")
            print("="*55)
        
        elif name == "channels" or name == "3" or name == "3️⃣":
            print("\n" + "="*55)
            print("   📢 TELEGRAM CHANNEL")
            print("   🔗 https://t.me/DA4K_HAcK")
            print("="*55)
        
        elif name == "developer" or name == "4" or name == "4️⃣":
            print("\n" + "="*55)
            print("   👨‍💻 DEVELOPER CONTACT")
            print("   🔗 https://t.me/GTDERBOT")
            print("="*55)
        
        elif name == "numberbot" or name == "5" or name == "5️⃣":
            print("\n" + "="*55)
            username = input("   👤 USERNAME: ")
            if username == 'GHOST':
                password = input("   🔑 PASSWORD: ")
                if password == '4882012':
                    print("   ✅ Access granted..!")
                    print("   🔗 https://t.me/NumberNest_2_Bot")
                    print("   🔗 https://t.me/Number_Nest_Bot")
                else:
                    print("   ❌ Wrong password!")
            else:
                print("   ❌ Wrong username!")
            print("="*55)
        
        else:
            print("\n" + "="*55)
            print("   ❌ Invalid service! Please choose from the list")
            print("   💡 Type 'exit' to quit")
            print("="*55)
        
        # رسالة انتظار قبل الرجوع للقائمة
        print("\n" + "─"*55)
        input("   ⏎ Press Enter to continue... ")
    
if __name__ == "__main__":
    main()
