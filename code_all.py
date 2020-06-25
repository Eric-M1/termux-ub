import os, datetime
import subprocess, re
import socket
from colorama import Fore, Style
from time import sleep

try:
      batteryH = open("/sys/class/power_supply/battery/capacity","r").read().replace("\n", '')
      ip = socket.gethostbyname(socket.gethostname())
      date = datetime.datetime.now().strftime("%H:%M:%S")
      def get_size():
            size = subprocess.check_output('du -sh /storage/emulated/0/', shell=True)
            sizeH = subprocess.check_output('du -sh /data/data/com.termux/files/home/', shell=True)
            file=open('.log.txt', "w") 
            file.write(str(size)+str(sizeH))
            file.close()
            
      get_size()
      os.system('clear')
      file = open('.log.txt', "r").read()
      filter = file.split('/')[0]
      sz = re.sub("b'|t|\\\|", '', filter)

      fileH = open('.log.txt', "r").read()
      filterH = file.split('/')[4]
      szH = re.sub("b|n|'|t|\\\|", '', filterH)

      print("""
                        Ｌ ｉ ｎ ｕ ｘ
      """)
      print(Style.BRIGHT + 'Tɪᴍᴇ:  ' + Fore.GREEN + Style.BRIGHT +date + Fore.RESET)
      print(Style.BRIGHT + 'Mʏ IP:  ' + Fore.GREEN + ip + Fore.RESET)
      print(Style.BRIGHT + 'Mᴇᴍᴏʀʏ:  ' + Fore.GREEN + sz + Fore.RESET)
      print(Style.BRIGHT + '$ Hᴏᴍᴇ:  ' + Fore.GREEN + szH + Fore.RESET)
      print(Style.BRIGHT + 'Bᴀᴛᴛᴇʀʏ:  ' + Fore.GREEN + str(batteryH) +'%'+ Style.RESET_ALL + Fore.RESET+'\n\n')
except:
    print('[!] Perhaps your paths are not so spaced')