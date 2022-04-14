#!/usr/bin/python3
import os
import subprocess
import cgi
import cgitb

# os.system("mkdir new_directory")
os.getpid()
##os.chmod("u", "+rwx")
os.chdir(r"C:\Users")

p = subprocess.Popen(
    ['dir'],
    stdout=subprocess.PIPE, shell=True)
output = p.communicate()[0]
print(output)