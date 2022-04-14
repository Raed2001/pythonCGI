#!/usr/bin/python3
import os
import subprocess

# os.system("mkdir new_directory")
os.getpid()
##os.chmod("u", "+rwx")
os.chdir(r"C:\Users")

p = subprocess.Popen(
    [r'cd C:\Users','dir'],
    stdout=subprocess.PIPE, shell=True)
output = p.communicate()[0]
print(output)