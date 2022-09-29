from time import sleep
from random import randint as rand

def dice_roll(sides, rolls):
        total = 0
        for i in range(rolls):
                a = rand(1, sides)
                total += a
                print(f'\n{sides}-sided die rolled...{a}!\n')
                sleep(1.5)
        print(f'Total: {total}\n')
        return total
n = int(input('\nInput the number of sides: '))
rolls = int(input('\nInput the number of rolls: '))
dice_roll(n, rolls)
