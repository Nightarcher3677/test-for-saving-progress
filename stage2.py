import time
import os

print('you see a codepad in front of you. next to it is a sign that says BRIDGE')
while 1 == 1:
    choice = input('above both of those signs, there is a screen that displays the words: CAPTAIN ANAGRAM \n it then flickers to read "lttree ot bunmre" then it flickers to ERROR 16 1 19 19 23 15 18 4  \n\nCode: ')
    if choice == 'password':
        print("as you enter the password (while making a mental note of the previous captain's lack of imagination), \n the screen flickers once more to reveal the words WELCOME CAPTAIN GANRAAM.")
        break
    else:
        print('The screen flickers and displays: INCORRECT PASSWORD')

print("you walk onto the bridge, and see the control panel. it's still running, as if the occupants had suddenly disappeared.")

while 1 == 1:
    choice = input('you can: look around, inpect control panel, poke chair \n\n')
    if choice == 'poke chair':
        print("wow, that's really soft")
    elif choice == 'look around':
        print('not much else to see')
    elif choice == 'inspect control panel':
        print('A radar function is still running, and shows a small dot moving towards you at approximately 760 km/h.')
        break
    else:
        print('that is not an action')
