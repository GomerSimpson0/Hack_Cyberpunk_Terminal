import random
from colorama import Fore, Back, init
import os
import sys

init()
number = [ [], [], [], [], [] ]
print(Fore.WHITE)

destination_numbers = []

def increment(n):
    n = n + 1

def destination():
    cache = random.randint(3, 5)
    boof = 0
    boof1 = 0
    boof2 = 0
    for i in range(cache):
        if i == 0:
            boof2 = random.randint(0, 4)
            boof = boof1
            destination_numbers.append(number[boof1][boof2])
        elif (i % 2) == 1:
            boof1 = random.randint(0, 4)
            while True:
                if boof1 == boof:
                    boof1 = random.randint(0, 4)
                    continue
                destination_numbers.append(number[boof1][boof2])
                boof = boof2
                break
        elif (i % 2) == 0:
            boof2 = random.randint(0, 4)
            while True:
                if boof2 == boof:
                    boof2 = random.randint(0, 4)
                    continue
                destination_numbers.append(number[boof1][boof2])
                boof = boof1
                break

def check_num(line, column, dest):
    if dest == number[column][line]:
        return True
    elif dest != number[column][line]:
        return False
        

def print_out(num, line_or_column): # True - column, False - line
    print('\n                             ')
    print('\t     1    2    3    4    5   ')
    print('\t   --------------------------')
    cache = random.randint(3, 5)
    print('\t1  | ', end = '')
    for i in range(5):
        for j in range(5):
            if (line_or_column == False) and (num == i):
                print(Fore.GREEN + Back.YELLOW + number[i][j] + Fore.WHITE + Back.BLACK, end = '')
                if j != 4:
                    print(' | ', end = '')
                elif (j == 4):
                    print(Back.BLACK + ' |')
                    print('\t   --------------------------')
                    if i != 4:
                        print('\t' + str(i + 2) + '  | ', end = '')
            elif (line_or_column == True) and (num == j):
                print(Fore.GREEN + Back.YELLOW + number[i][j] + Fore.WHITE + Back.BLACK, end = '')
                if j != 4:
                    print(' | ', end = '')
                elif (j == 4):
                    print(Back.BLACK + ' |')
                    print('\t   --------------------------')
                    if i != 4:
                        print('\t' + str(i + 2) + '  | ', end = '')

            else:
                print(Back.BLACK + Fore.GREEN + number[i][j] + Fore.WHITE, end = '')
                if j != 4:
                    print(' | ', end = '')
                elif (j == 4):
                    print(' |')
                    print('\t   --------------------------')
                    if i != 4:
                        print('\t' + str(i + 2) + '  | ', end = '')


def main():
    print("Hello! Lets hack terminal like in Cyberpunk 2077")
    input('\nPress enter when you will ready . . .')
    os.system('clear')
    for i in range(5):
        for j in range(5):
            cache = random.randint(1, 4)
            if cache == 1:
                number[i].append('A9')
            elif cache == 2:
                number[i].append('B7')
            elif cache == 3:
                number[i].append('N5')
            elif cache == 4:
                number[i].append('S3')
    destination()
    print_out(0, False)
    print('\n\n ', 'Destination: ', end = '')
    boof_line = 0
    boof_column = 0
    color_for_destination = 0
    for i in range(len(destination_numbers)):
        if color_for_destination < i:
            print(Fore.WHITE, end = '')
        if color_for_destination > i:
            print(Fore.GREEN, end = '')
        if color_for_destination == i:
            print(Fore.CYAN, end = '')
        print(str(destination_numbers[i]) + '  ', end = '')
    color_for_destination = color_for_destination + 1
    boof_choice = 0
    for i in range(len(destination_numbers)):
        if (i % 2) == 0:
            choice = int(input("\n\n  " + Fore.WHITE + "Input number of column: "))
            boof_column = choice
            if i == 0:
                if check_num((boof_column - 1), boof_line, destination_numbers[i]) == True:
                    os.system('clear')
                    if i != len(destination_numbers) - 1:
                        print_out((choice - 1), True)
                    elif i == len(destination_numbers) - 1:
                        print_out(boof_choice, False)
                    print('\n\n ', 'Destination: ', end = '')
                    for i in range(len(destination_numbers)):
                        if color_for_destination > i:
                            print(Fore.GREEN, end = '')
                        if color_for_destination == i:
                            print(Fore.CYAN, end = '')
                        if color_for_destination < i:
                            print(Fore.WHITE, end = '')
                        print(str(destination_numbers[i]) + '  ', end = '')
                    color_for_destination = color_for_destination + 1
                    boof_choice = choice - 1
                else:
                    os.system('clear')
                    print_out(boof_choice, False)
                    print('\n\n ', 'Destination: ', end = '')
                    for i in range(len(destination_numbers)):
                        if color_for_destination > i:
                            print(Fore.GREEN, end = '')
                        if (color_for_destination - 1) == i:
                            print(Fore.RED, end = '')
                        if color_for_destination <= i:
                            print(Fore.WHITE, end = '')
                        print(str(destination_numbers[i]) + '  ', end = '')
                    color_for_destination = color_for_destination + 1
                    print('\n\n     ' + Fore.RED + '      ACCESS DENIED\n\n')
                    sys.exit(0)

            else:
                if check_num((boof_column - 1), (boof_line - 1), destination_numbers[i]) == True:
                    os.system('clear')
                    if i != len(destination_numbers) - 1:
                        print_out((choice - 1), True)
                    elif i == len(destination_numbers) - 1:
                        print_out(boof_choice, False)
                    print('\n\n ', 'Destination: ', end = '')
                    for i in range(len(destination_numbers)):
                        if color_for_destination > i:
                            print(Fore.GREEN, end = '')
                        if color_for_destination == i:
                            print(Fore.CYAN, end = '')
                        if color_for_destination < i:
                            print(Fore.WHITE, end = '')
                        print(str(destination_numbers[i]) + '  ', end = '')
                    color_for_destination = color_for_destination + 1
                    boof_choice = choice - 1
                else:
                    os.system('clear')
                    print_out(boof_choice, False)
                    print('\n\n ', 'Destination: ', end = '')
                    for i in range(len(destination_numbers)):
                        if color_for_destination > i:
                            print(Fore.GREEN, end = '')
                        if (color_for_destination - 1) == i:
                            print(Fore.RED, end = '')
                        if color_for_destination <= i:
                            print(Fore.WHITE, end = '')
                        print(str(destination_numbers[i]) + '  ', end = '')
                    color_for_destination = color_for_destination + 1
                    print('\n\n     ' + Fore.RED + '      ACCESS DENIED\n\n')
                    sys.exit(0)


        else:
            choice = int(input('\n\n  ' + Fore.WHITE + 'Input number of line: '))
            boof_line = choice
            if check_num((boof_column - 1), (boof_line - 1), destination_numbers[i]) == True:
                os.system('clear')
                if i != len(destination_numbers) - 1:
                    print_out((choice - 1), False)
                elif i == len(destination_numbers) - 1:
                    print_out(boof_choice, True)
                print('\n\n ', 'Destination: ', end = '')
                for i in range(len(destination_numbers)):
                    if color_for_destination > i:
                        print(Fore.GREEN, end = '')
                    if color_for_destination == i:
                        print(Fore.CYAN, end = '')
                    if color_for_destination < i:
                        print(Fore.WHITE, end = '')
                    print(str(destination_numbers[i]) + '  ', end = '')
                color_for_destination = color_for_destination + 1
            else:
                os.system('clear')
                print_out(boof_choice, True)
                print('\n\n ', 'Destination: ', end = '')
                for i in range(len(destination_numbers)):
                    if color_for_destination > i:
                        print(Fore.GREEN, end = '')
                    if (color_for_destination - 1) == i:
                        print(Fore.RED, end = '')
                    if color_for_destination <= i:
                        print(Fore.WHITE, end = '')
                    print(str(destination_numbers[i]) + '  ', end = '')
                color_for_destination = color_for_destination + 1
                print('\n\n     ' + Fore.RED + '      ACCESS DENIED\n\n')
                sys.exit(0)
            boof_choice = choice - 1

    print('\n\n     ' + Fore.GREEN + '      ACCESS GRANTED\n\n')
    sys.exit(0)

main()
