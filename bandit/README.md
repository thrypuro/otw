host : bandit.labs.overthewire.org
port : 2220

`ssh banditx@bandit.labs.overthewire.org -p 2220`
logging in with private key
`ssh -i banditx.key banditx@bandit.labs.overthewire.org -p 2220`


## bandit1 : boJ9jbbUNNfktd78OOpsqOltutMc3MY1 

```bash
cat <-
```


## bandit2 : CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

cat again

## bandit3 : UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

cat, ls -la?

## bandit4 : pIwrPrtPN36QITSp3EQaw936yaFoFgAB

`grep -r .` looks through everything in the directory

## bandit5 : koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```bash
find ./ -type f -size 1033c ! -executable  
cat ./maybehere07/.file2
```

## bandit6 : DXjZPULLxYr17uwoI01bNLQbtFemEgo7
My solution and then just find the file that doesnt error 
```bash
find / -group "bandit6" -user "bandit7" -size 33c
```
good solution
```bash
find / -user bandit7 -group bandit6 -size 33c -type f 2>/dev/null
```
`2>/dev/null` - https://linuxhint.com/two-dev-null-command-purpose/

## bandit7 : HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

grep lol

## bandit8 : cvX2JJa4CFALtqS87jk27qwqGhBM9plV
unique occurance 
```bash
cat data.txt | sort | uniq -u
```

## bandit9 : UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```bash
strings data.txt
```

## bandit10 : truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```bash
cat data.txt | base64 -d
```

## bandit11 : IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```bash
alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
cat data.txt | rot13
```

## bandit12 : 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

```bash
tar -xvf datax.bin
bzip2 -d datax.bz2
gzip -d datax.gz
```

## bandit13 : 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
just ssh key login
https://docs.rackspace.com/support/how-to/logging-in-with-an-ssh-private-key-on-linuxmac/

## bandit14 : 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
just net cat and post the pass from this chall

## bandit15 : BfMYroe26WYalil77FoDi9qh59eK5xNr
https://superuser.com/questions/346958/can-the-telnet-or-netcat-clients-communicate-over-ssl
really cool `openssl s_client -connect host:port`

## bandit16 :  cluFn7wTiGryunymYOu4RcffSxQluehd
```bash
nmap  -p 31000-32000 localhost -sV # slow but gets all the relevant ones

```

## bandit17: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
use diff lol

## bandit18: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
`ssh banditx@bandit.labs.overthewire.org -p 2220 cat readme`

## bandit19 : IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
execute command from binary
https://en.wikipedia.org/wiki/Setuid
setuid is a method giving temporary elevated priveledges for users to perform a certain task.

## bandit20 : GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```bash
screen -S aa
ctrl A + d to dettach
echo 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j' | nc -nvlp 8080
```

## bandit21 : gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

Straightforward look at the cronscripts and cat the file

## bandit22 : Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

same thing but md5 hash

## bandit23 : UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
make a bash script
```bash
#!/bin/bash  
  
cat /etc/bandit_pass/bandit24 > /tmp/bruh/password.txt
```
gib the appropriate perms
really useful link to learn about permission https://chmodcommand.com/chmod-777/
```bash
chmod -R 777 bashscript
touch password.txt
chmod -R 777 password.txt
```
make sure to change permission for password so it can be written to by anyone.
everytime you edit these files, the permission gets changed :weary:, but this works lol

## bandit24 : UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```bash
#!/bin/bash
passwd24=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
for i in {0000..9999}; do
            echo "$passwd24 $i"
done | nc localhost 30002  | grep -v Wrong | grep -v "I am the pincode checker for user bandit25"

```
shitty bruteforce cbb
grep -v is cool ig

## bandit25 : uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
VERY convoluted chall WAAAA
so more is a command that views text, secretly a vi editor if the text isnt big enough, anyway, you then execute commands in vi to change the shell 
`:set shell=/bin/bash` then `:sh` will exit to bash bingo
https://superuser.com/questions/287994/how-to-specify-shell-for-vim this helped solve

## bandit26 : 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
free flag because the other one annoying lol

## bandit27 : 3ba3118a22e93127a4ed485be72ef5ea
ez git stuff

## bandit28 : 0ef186ac70e04ea33b4c1853d2526fa2
git checkout moment
```bash
git log --reflog
```
cli to list all the commits

## bandit29 : bbc96594b4e001778eee9975372716b2
pretty cool
```bash
git branch -a # views all the branches
git checkout branchname
```

## bandit30 :5b90576bedb2cc04c86a9e924ce42faf
tags are github things that let you mark a specific point etc
```bash
git tags
git show secret
```
 
## bandit31 : 47e603bb428404d265f59c42920d81e5

easy  git push

## bandit32 : 56a9bf19c63d650ce78e6ec0354ee45e
`$0`

## bandit33 : c9c3199ddf4121b10cf581a98d51caee

FIN