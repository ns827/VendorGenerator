import os
import sys
from time import sleep
from termcolor import colored
from datetime import datetime

#  ############# M A N I F E S T ##############

version = '0.1b'
time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
head = """
#################################################
# vendor-blobs.mk                               #
# Generated by VendorGenerator - Automatically! #
# VenderGenerator version: %s                 #
# Generated on: %s             #
#################################################

""" % (version, time)
sndhead = "PRODUCT_COPY_FILES +="

#  ############# M A N I F E S T ##############


print('\033[01;36mAndroid vendor-blobs.mk generator')
sleep(.1)
if len(sys.argv) < 3 :
    print(colored("[!] Usage: " + sys.argv[0] + " <vendor name> <product name>", 'red'))
else:
    print("[*] Generating vender-blobs.mk for vendor/" + sys.argv[1] + '/' + sys.argv[2] + " folder\033[0;0m")
    sleep(.2)

    rt = os.popen('find vendor/' + sys.argv[1] + "/" + sys.argv[2] + "/proprietary").read()
    file_list = rt.split("\n")[1:]
    file_list = file_list[:len(file_list) - 1]
    if file_list == ['']:
        print(colored("[!] Couldn't find any file/folder in vendor/" + sys.argv[1] + "/" + sys.argv[2] + "/proprietary folder: sys.exiting.", 'red'))
        print(colored("[!] Did you put pre-built files on that folder?", 'red'))
    elif not file_list:
        print(colored("[!] Error while processing find command: sys.exiting.", 'red'))
        print(colored("[!] Maybe you should create that directory but you haven't"), 'red')
    else:
        delList = []

        for i in range(len(file_list)):
            if os.path.isdir(file_list[i]):
                print("[-] " + file_list[i] + " is a directory: ignoring.")
                delList.append(i)

        dels = 0

        for i in delList:
            del file_list[i - dels]
            dels += 1

        file_value = ""
        file_value += head + sndhead
        for i in file_list:
            file_value += " \\\n    " + i
        print("\033[01;36m[*] Saving makefile: vendor/" + sys.argv[1] + "/" + sys.argv[2] + "/vendor-blobs.mk\033[0;0m")
        print(file_value)
        file = open("vendor/" + sys.argv[1] + "/" + sys.argv[2] + "/vendor-blobs.mk", 'w')
        file.write(file_value)
        file.close()
        print("\n\033[36m[*] Done!")