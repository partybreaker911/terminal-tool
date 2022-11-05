import socket
import logging

from conf import (
       TOKEN, IRC_SERVER, IRC_CHANNEL, IRC_PORT,
       IRC_NICKNAME
        )

sock = socket.socket()

sock.connect((IRC_SERVER, int(IRC_PORT)))

sock.send(f"PASS {TOKEN}\n".encode("utf-8"))
sock.send(f"NICK {IRC_NICKNAME}\n".encode("utf-8"))
sock.send(f"JOIN {IRC_CHANNEL}\n".encode("utf-8"))

resp = sock.recv(2048).decode('utf-8')

print(resp)

#sock.close()

