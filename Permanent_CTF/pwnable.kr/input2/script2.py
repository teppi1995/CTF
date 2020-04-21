import subprocess
import os
import socket
import time

os.mkdir("/tmp/aiueo")
os.chdir("/tmp/aiueo")
os.symlink("/home/input2/flag", "/tmp/aiueo/flag")

# stage1
arg=["a" for i in range(100)]
arg[ord("A")] = ""
arg[ord("B")] = "\x20\x0a\x0d"
arg[ord("C")] = "40001"

#stage2
stdinr, stdinw = os.pipe()
stderrr, stderrw = os.pipe()

os.write(stdinw, "\x00\x0a\x00\xff")
os.write(stderrw,"\x00\x0a\x02\xff")

#stage3
os.environ["\xde\xad\xbe\xef"] = "\xca\xfe\xba\xbe"

#stage4
with open("/tmp/aiueo/\x0a", "wb") as f:
    f.write("\x00\x00\x00\x00")


s = subprocess.Popen(["/home/input2/input"]+arg[1:], stdin = stdinr, stderr = stderrr)

time.sleep(3)

print(s)
#stage5
#stage5
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 40001))
client.send("\xde\xad\xbe\xef")
client.close()
