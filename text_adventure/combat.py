

import sys
import os
import random
import time


health = 100
npc_health = 100


def s_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)



def menu():
    s_print('Welcome to "Box Until You Die" where you box until you die!')
    s_print(' Are you ready to fight?')
    while True:
        action = input('\n>')
        if action == 'yes':
            s_print("Excellent!  Let's go!")
            time.sleep(1)
            print()
            first_turn()
        else:
            s_print("Oh...  Well too bad!  FIGHT!")
            print()
            first_turn()


def first_turn():
    s_print("Just in case it wasn't clear, here are your options: punch, Punch, or PUNCH!")
    print('\n>Type: "punch" to punch')
    while True:
        action = input('\n>')
        if action == 'punch':
            punch()


def combat_turn():
    print('Options: Punch')
    while True:
        action = input('\n>')
        if action == 'punch':
            punch()


def punch():
    global npc_health
    print('You punch your opponent!')
    dmg = random.randint(1,10)
    npc_health -= dmg
    print('You dealt',dmg,'damage.')
    if npc_health > 75:
        print('He looks unfazed.')
        print()
        npc_attack()
    elif npc_health > 50:
        print('He looks slightly battered.')
        print()
        npc_attack()
    elif npc_health > 25:
        print('He looks beaten and bloody.')
        print()
        npc_attack()
    elif npc_health > 0:
        print("He is at death's door.")
        print()
        npc_attack()
    elif npc_health <=0:
        s_print("Hey!  You killed him!  Go rest up for the next match.")
        time.sleep(1)
        print()
        restart()


def npc_attack():
    global health
    print('Your opponent punches you!')
    dmg = random.randint(1,10)
    health -= dmg
    print('You take',dmg,"damage!")
    print('You have',health,'health remaining.')
    print()
    if health <= 0:
        s_print("Oh no!  You're dead.  Better luck next time.")
        s_print('\n>GAME OVER')
        time.sleep(1)
        print()
        restart()
    else:
        combat_turn()


def restart():
    global health
    global npc_health
    health = 100
    npc_health = 100
    menu()


menu()