from pwn import *
context.arch = 'amd64'
write('flag', 'This is the flag\n')
sc = shellcraft.cat('flag')
print(asm(sc))
