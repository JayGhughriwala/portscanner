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
print("\n\n")
print("Scanning target : " + target)
print("Time Started : " + str(datetime.now()))
print("$" * 50)
print("\n\n")

try:
    for port in range(50, 85):  # you can set your range according to your preferences
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open")
        s.close()


except KeyBoardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("could not connect to server")
    sys.exit()
