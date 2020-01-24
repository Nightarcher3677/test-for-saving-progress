import time
import os
import random
x = 1
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
        chair = 1
    elif choice == 'look around':
        print('not much else to see')
    elif choice == 'inspect control panel':
        print('A radar function is still running, and shows a small dot moving towards you at approximately 760 km/h.')
        break
    else:
        print('that is not an action')
print('you jam your finger on the home button that is displayed on the lower right corner, and activate the shields program. the ship approaches you.')
print('(this can cause the story to diverge) the ship approaching you attempts to make contact.')
while 1 == 1:
    choice = input('do you: accept the call [y], deny the call [n]')
    if choice == 'y':
        print("you have accepted the call")
        accepted = True
        break
    elif choice == 'n':
        print('you have denied the call')
        accepted = False
        break
    else:
        print('that is not an action')
if accepted == True:
    print('A holographic screen appears before you, showing the face of a man who appeared to be in his early thirties \n, his left eye replaced with a shiny black lens that must have been the end of a camera')
else:
    print('the ship, now in range of your vision, fires on you. Your shields are at 96%')

    while x == 1:
        sh = 96
        choice = input('do you: fire back, run away')
        if choice == 'fire back':
            print("you fire back. the blast brings their shields down to 98%")
            sh = 96
            eh = 98
            p = 1
            while p == 1:
                if eh > 0:
                    choice = input('you can: fire, run')
                    if choice == 'fire':
                        eh = eh - random.randint(1,6)
                        print("the enemy ship's shields are at " + str(eh) + '%')
                        sh = sh - random.randint(1,5)
                        print("your ship's shields are at " + str(sh) + '%')
                    elif choice == 'run':
                        run = random.randint(1,15)
                        if run == 1:
                            print('Your ship blasts in the opposite direction to the enemy ship, which is crushed \n by a passing asteroid (how convenient)')
                            break
                        else:
                            print('the enemy ship follows you, and blasts you before you can get away')
                            sh = sh - random.randint(1,5)
                            print("your ship's shields are at " + str(sh) + '%')
                elif sh < 0:
                    print('you died. better luck next time! (just kidding! you suck at this)')
                    break
                else:
                    print('the enemy ship is destroyed by your final blast, and the debris is scattered throughout space')
                    x = 2
                    break
        elif choice == 'run away':
            run = random.randint(1,15)
            if run == 1:
                print('Your ship blasts in the opposite direction to the enemy ship, which is crushed \n by a passing asteroid (how convenient)')
                x = 2
                break
            else:
                print('the enemy ship follows you, and blasts you before you can get away')
                sh = sh - random.randint(1,5)
                print("your ship's shields are at " + str(sh) + '%')
                choice = 'fire back'
        else:
            print('that is not an action')
if chair == 1:
    print('with the enemy ship gone, you can finally relax. you poke the chair, as if it would have somehow become hard. it is still soft')
else:
    print('with the enemy ship gone, you can finally relax.')

s = open('stage.txt', 'w')
s.write('stage3')
s = open('stage.txt', 'r')
read = s.read()
hg = input('you can now safely press the X button without losing your progress \n\n')
os.popen('stage3.py')
