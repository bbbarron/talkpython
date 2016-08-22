"""
Game of wizard (wizard app) from Talk Python to Me class. This copy modified
for study purposes.


bbarron
8/22/2016

"""

import time
import random

from players import Wizard, Creature, SmallAnimal, Dragon # this llows calling objects without full name

# todo: modify scoring to add hero strength as he defeats more foes

def main():
    print_header()
    game_loop()


def print_header():
    # Yes, I added this after I recorded the video
    # but I thought you'd get a kick out if it. ;)
    print()
    print('-----------------------------------------------------------------------')
    print('''
   (  )   /\   _                 (
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \\
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
     WIZARD BATTLE        )        \_____________  `              \  /
(__       APP      +- .( -'.- <. - _  VVVVVVV VaV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \\
    ''')
    print()
    print('-----------------------------------------------------------------------')
    print()

def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 10, True),
        Wizard('Evil Wizard', 300)
    ]
    # todo - modify strength of dragon to make him beatable
    # print(creatures)

    hero = Wizard('Gandolf', 100)

    while True:

        active_creature = random.choice(creatures)
        # todo: can this be changed to random setting (after runaway?)
        print('A {} of level {} has appear from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            # todo - change, don't remove small creatures, allow unlimited

            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name)) # todo add strength of hero to print
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
    main()
