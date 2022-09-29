from time import sleep
from random import randint as rand

def dice_roll(sides, rolls):
        total = 0
        values = []
        
        for i in range(rolls):
                a = rand(1, sides)
                values.append(a)
                print(f'\n{sides}-sided die rolled...{a}!\n')
                sleep(1.5)
        
        if len(values) > 1:
                values.sort()
                print(f'{values[0]} was the lowest value. Dropping {values[0]} from the total...\n')
                values.pop(0)
                sleep(1)
        
        for number in values:
                total += number
        
        print(f'Total: {total}\n')
        return total


n = int(input('\nInput the number of sides: '))
rolls = int(input('\nInput the number of rolls: '))
dice_roll(n, rolls)
