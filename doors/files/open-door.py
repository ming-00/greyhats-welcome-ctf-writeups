# pwntools is a very powerful library for doing exploitation
from pwn import *

# update with actual values
HOST = "challs1.nusgreyhats.org"
PORT = 5301

# . to open a connection to the remote service, aka the challenge
r = remote(HOST, PORT)  
# . use process instead of remote to execute the local version of the program
# r = process(BINARY)   
pause()

# TODO: Fill in your payload
r.sendline(str(int('0x942246', 16)))    # door 1 9708102
r.sendline("992428")                    # door 2 992428
r.sendline("2187324")                   # door 3 2187324
r.sendline("612381")                    # door 4 612381

# earlier, the script helps us send/receive data to/from the service
# with interactive, we can directly interact with the service
r.interactive()