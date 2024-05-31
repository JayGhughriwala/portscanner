# print("TEST ")

import sys
import socket
from datetime import datetime


# define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translagte hostname to ipv4


else:
    print("invalid amount of arguments")
    print("Syntax: python3 scanner.py  <ip>")


# add a nice banner

print("$" * 50)
print("Scanning target : " + target)
print("Time Started : " + str(datetime.now()))
print("$" * 50)
