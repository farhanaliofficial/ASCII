#coded by Farhan Ali
#github @farhanaliofficial

import os,sys

os.system("pkg install figlet")
os.system("clear")
def main():
 logo = """
    \033[1;32;40m  _____          _                      _    _ _
    \033[1;31;40m |  ___|_ _ _ __| |__   __ _ _ __      / \  | (_)
    \033[1;32;40m | |_ / _` | '__| '_ \ / _` | '_ \    / _ \ | | |
    \033[1;31;40m |  _| (_| | |  | | | | (_| | | | |  / ___ \| | |
    \033[1;32;40m |_|  \__,_|_|  |_| |_|\__,_|_| |_| /_/   \_\_|_|
 """

 print(logo)
 print("")
 print("\033[1;31;40m    -------------------------------------------------")
 print("    \033[1;36;40mCoded By Farhan Ali")
 print("    \033[1;36;40mGithub @farhanaliofficial")
 print("\033[1;31;40m    -------------------------------------------------")
 print("")
 inp = input("\033[1;33;40mEnter Text: ")
 print("\033[1;35;40m")
 os.system("figlet "+inp)
 print("")
main()
def close():
 print("\033[1;36;40mPress Ctrl + Z to Exit!")
 tryagain = input("\033[1;36;40mTry Again? Press Enter!")
 if tryagain == "":
  os.system("clear")
  main()
  close()

close()