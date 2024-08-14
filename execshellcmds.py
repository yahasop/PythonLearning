#!/usr/bin/env python3

import subprocess

#The subprocess.run() method will execute a shell command. Then returns a CompletedProcess instance with at least atributes args (command) and returncode. Also, it doesnt capture stdout and stderr by default so a PIPE keyword must be passed to stdout and stderr in order to capture them.
proc = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

#This new process will fail. We need to set check=True to ensure a CalledErrorException exception is raised. Otherwise, even if the command fails, the instruction will throw a 0 code, meaning a succesful execution.
new_proc = subprocess.run(["cat", "filaname"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)# check=True)

#The results of the pipes are bytes, not string. This is identified with the preceding b before what we think is a string if we call proc.stdout. Newline characters are there but they are no interpreted as they exist in a byte type object. To convert bytes into strings we use the decode() bytes method.
print(proc.stdout.decode()) #A byte to string conversion
print(new_proc.stderr) #A raw byte
