#!/usr/bin/python3
import sys
file_names = sys.argv{1:]
print(file_names)
for i in file_names:
    f = open(i,'w')
    f.close()
# it must not replace any existing files
# if there is an existing directory/file than it must not throw an error
# if there is a object than update current time but do not edit this file
