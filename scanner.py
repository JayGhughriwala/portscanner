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
