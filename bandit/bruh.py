from pwn import *
import ctypes
libgcc_s = ctypes.CDLL('libgcc_s.so.1')
r = remote('127.0.0.1',30002)

print(r.recvline())
