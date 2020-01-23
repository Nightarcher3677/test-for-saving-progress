import time

print("You hear a voice crackle through a radio 'Is anyone there!? Hello?! Mayda-'")
print("the radio cuts out and you see a brilliant starburst of yellow, white and orange.")
print("you turn to leave the room, but see that the bulkhead seperating you from the rest of the ship is locked.")
cry = '1'
while cry == '1':
    choice = input('what do you do? you can: look around, cry \n\n')
    if choice == 'cry':
        print('stop wasting time, you wimp')
    elif choice == 'look around':
        cry = '2'
    else:
        print('that is not an action')

print('as you look around, you see: a window leading to the the empty void of space, a bulkhead door,')
print('a bed, and a paperclip. what will you do?')
while 1 == 1:
    choice = input('you can: take paperclip, sleep, open window \n\n')
    if choice == 'open window':
        print('wow, you really are stupid')
        print('as you open the window, you realise that you are in fact in space.')
        print('you get sucked out the window and die')
        print('respawning...')
        time.sleep(1)
    elif choice == 'take paperclip':
        print('you have taken the paperclip')
        break
    elif choice == 'sleep':
        print('you take a nap')
        time.sleep(1)
        print('you have accomplished nothing')
    else:
        print('that is not an action')
print('you have taken the paperclip')

while 1 == 1:
    choice = input('you can: pick bulkhead, open window, sleep \n\n')
    if choice == 'open window':
        print('wow, you really are stupid')
        print('as you open the window, you realise that you are in fact in space.')
        print('you get sucked out the window and die')
        print('respawning...')
        time.sleep(1)
    elif choice == 'pick bulkhead':
        print('you have picked the bulkhead. It is no longer locked')
        break
    elif choice == 'sleep':
        print('you take a nap')
        time.sleep(1)
        print('you have accomplished nothing')
    else:
        print('that is not an action')

while 1 == 1:
    choice = input('you can: open bulkhead, open window, sleep \n\n')
    if choice == 'open window':
        print('wow, you really are stupid')
        print('as you open the window, you realise that you are in fact in space.')
        print('you get sucked out the window and die')
        print('respawning...')
        time.sleep(1)
    elif choice == 'open bulkhead':
        print('you open the bulkhead')
        break
    elif choice == 'sleep':
        print('you take a nap')
        time.sleep(1)
        print('you have accomplished nothing')
    else:
        print('that is not an action')


print('beyond the bulkhead there is a corridor lined with fluorescent strips of light. through a window along the right side you can see debris from the ship you heard earlier')
print('on the left side of the corridor, it says HERMES GALACTIC CLASS. It is then that you realise that you have no recollection of')
print('who you are. It appears you have amnesia. The only thought you can muster is: how cliché')
print('you continue down the corridor...')
print('you have completed stage one!! press ENTER to move on to the next stage')
s = open('stage.txt', 'w')
s.write('stage2')
s = open('stage.txt', 'r')
read = s.read()
hg = input('you can now safely press the X button without losing your progress \n\n')
os.popen('stage2.py')
