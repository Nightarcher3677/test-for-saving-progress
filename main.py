import time
import tkinter
import subprocess
import os

#loading stage

s = open('stage.txt', 'a')
s = open('stage.txt', 'r')
print('your current stage is ' + s.read())
k = '1'
while k == '1' :
    i = input('enter [l] to load save or [n] for a new save \n\n')
    if i == 'l':
        read = s.read()
        os.popen(read + '.py')
        k = '2'
    elif i == 'n':
        s = open('stage.txt', 'w')
        s.write('stage 1')
        s = open('stage.txt', 'r')
        read = s.read()
        os.popen(read + '.py')
        k = '2'
