#!/usr/bin/python3
import os
import subprocess

os.system("mkdir verzeichnis")
os.mkdir("verzeichnis_name")
os.getpid()
os.chmod("", "")

p = subprocess.Popen(
['ls', '-la'],
stdout=subprocess.PIPE)
output = p.communicate()[0]
print(output)