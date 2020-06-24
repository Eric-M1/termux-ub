import os 
import shutil
import subprocess
from time import sleep

os.system('clear')
print('''
[#] Choose an operating mode:
[+] 1 - Linux and time
[+] 2 - Linux and all
[+] 3 - Empty console
''')

n_o = input('[~] Choose function: ')

try:
    # ---- code_ld.py
    if n_o == '1':
        if os.path.exists("/data/data/com.termux/files/usr/etc/code_all.py"):
            os.remove("/data/data/com.termux/files/usr/etc/code_all.py")
            print('[-] Saved file deleted!')
            
        elif os.path.exists("/data/data/com.termux/files/usr/etc/code_ld.py"):    
            os.remove("/data/data/com.termux/files/usr/etc/code_ld.py")
            print('[-] Saved file deleted!')
            
        elif os.path.exists("/data/data/com.termux/files/usr/etc/motd"):
            os.remove("/data/data/com.termux/files/usr/etc/motd")
            
        shutil.copy2("code_ld.py", "/data/data/com.termux/files/usr/etc/")

        open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w').write('''if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
            /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
    fi

    PS1='> '
    python /data/data/com.termux/files/usr/etc/code_ld.py''')
        print('[+] Installation...')
        print('[#] Reboot console ')
        sleep(1.5)

    # ---- code_all.py
    elif n_o == '2':
        if os.path.exists("/data/data/com.termux/files/usr/etc/code_all.py"):
            os.remove("/data/data/com.termux/files/usr/etc/code_all.py")
            print('[-] Saved file deleted!')
            
        elif os.path.exists("/data/data/com.termux/files/usr/etc/code_ld.py"):    
            os.remove("/data/data/com.termux/files/usr/etc/code_ld.py")
            print('[-] Saved file deleted!')
        
        elif os.path.exists("/data/data/com.termux/files/usr/etc/motd"):
            os.remove("/data/data/com.termux/files/usr/etc/motd")
            
        shutil.copy2("code_all.py", "/data/data/com.termux/files/usr/etc/")
        open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w').write('''if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
            /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
    fi

    PS1='> '
    python /data/data/com.termux/files/usr/etc/code_all.py''')
        print('[+] Installation...')
        print('[#] Reboot console')
        sleep(1.5)

    # ---- Empty
    elif n_o == '3':
        if os.path.exists("/data/data/com.termux/files/usr/etc/code_all.py"):
            os.remove("/data/data/com.termux/files/usr/etc/code_all.py")
            print('[-] Saved file deleted!')
            
        elif os.path.exists("/data/data/com.termux/files/usr/etc/code_ld.py"):    
            os.remove("/data/data/com.termux/files/usr/etc/code_ld.py")
            print('[-] Saved file deleted!')

        open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w').write('''if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
            /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
    fi

    PS1='$ '
    clear''')
        print('[+] Installation...')
        print('[#] Reboot console ')
        sleep(1.5)

    else:
        print('[!] Choose function!')
        pass
except:
    print('[!] Perhaps your paths are not so spaced')
