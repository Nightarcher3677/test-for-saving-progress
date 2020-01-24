import os

s = open('stage.txt', 'a')
s = open('stage.txt', 'r')
j = s.read()
print('your current stage is ' + j)
q = 1
stage = input('pick your stage (1, 2, 3) \n\n')
while q == 1:
    if stage == '1':
        os.popen('stage1.py')
        break
    elif stage == '2':
        os.popen('stage2.py')
        break
    elif stage == '3':
        os.popen('stage3.py')
        break
