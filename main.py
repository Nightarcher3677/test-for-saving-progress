import time

import subprocess
import os
stage = '0'
#loading stage

s = open('stage.txt', 'a')
s = open('stage.txt', 'r')
j = s.read()
print('your current stage is ' + j)
if j == 'stage1':
    stage = '1'
k = '1'
while k == '1':
    i = input('enter [l] to load save or [n] for a new save \n\n')
    if i == 'l':
        os.popen('stagepick.py')

    elif i == 'n':
        s = open('stage.txt', 'w')
        s.write('stage1')
        s = open('stage.txt', 'r')
        read = s.read()
        os.popen(read + ".py")
        k = '2'
