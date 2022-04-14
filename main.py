#!/usr/bin/python3
import os
import subprocess

# os.system("mkdir new_directory")
os.getpid()
##os.chmod("u", "+rwx")

p = subprocess.Popen(
    ['ls', '-la'],
    stdout=subprocess.PIPE, shell=True)
output = p.communicate()[0]
print(output)