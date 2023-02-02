#!/usr/bin/python3

import os
option = input("[+] Select the path of the target: \n"
        ">> Example: /home/kali/Downloads/kali.ovpn \n"
        ">> ")
os.system("mv " + option + " .")
