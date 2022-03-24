from pwn import *
context.arch = 'amd64'
sc = shellcraft.sh()
print(asm(sc))
