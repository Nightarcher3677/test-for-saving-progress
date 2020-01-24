import time

print('now that you have disposed yourself of the enemy ship, your radar is showing you something new.')
print("a planet's orbit has brought it into range of your scanners and a signal is hailing from it.")

while 1 == 1:
    choice = input('do you answer? yes, no \n\n')
    if choice == 'yes':
        print("you answer the call")
        break
    elif choice == 'no':
        print('too bad')
        break
    else:
        print('that is not an action')

print('the space pirate that you killed (because logic) appears before you on a holographic display')
s = open('enemy.txt', 'a')
s = open('enemy.txt', 'r')
j = s.read()
if j == 'yes':
    print("you begin to feel nostalgic")

print("the pirate says: you thought you'd seen the last of me, didn't you?! after all these years... well! now- 'wait.' you cut in 'it's been, like less than a minute. also, you got hit by an asteroid, remember?")
print("the pirate thinks for a moment, and then says: 'oh well, it was fun while it lasted' then disappears before your eyes")

while 1 == 1:
    choice = input('you can: land on the planet, sleep, poke chair')
    if choice == 'land on the planet':
        print('you begin the descent onto the planet')
        break
    elif choice == 'poke chair':
        print('that is very soft')
    elif choice == 'sleep':
        print('you take a nap')
        time.sleep(1)
        print('you have accomplished nothing')
    else:
        print('that is not an action')

print('your ship begins to fly towards the planet. soonyou realise that you are going too fast (2000km/h) you are nearly in the atmosphere')

while 1 == 1:
    choice = input('you can: slow down, sleep \n\n')
    if choice == 'sleep':
        print('as you go to sleep, you realise that your ship is still hurtling towards a planet')
        print('congratulations. you died')
        print('respawning...')
        time.sleep(1)
    elif choice == 'slow down':
        print('you slow the ship down')
        break
    else:
        print('that is not an action')
print('you miraculously slow down in time for a safe landing.')
print('you look around you. the ground is made of clay, with a thin layer of water over it, presumably from the last rain.')
print('you wade throught the water, as the rest of the planet curves around you. it is as if you are in the center of a hollow planet.')




fgf = input("press ENTER to continue")
