import os

s = open('stage.txt', 'a')
s = open('stage.txt', 'r')
j = s.read()
print('your current stage is ' + j)

stage = input('pick your stage (1, 2, branch1, branch2) \n\n')

if stage == '1':
    os.popen('stage1.py')
elif stage == '2':
    os.popen('stage2.py')
