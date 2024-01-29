from config import CHARACTERS
from colors import Color
from time import sleep
from os import system


def title():
    print(Color.bold + '\n                    Extended Caesar Cipher By:                ')
    print(Color.reset)
    sleep(0.2)
    print(Color.red + ' @@@@@@   @@@  @@@  @@@  @@@  @@@@@@@        @@@  @@@  @@@  @@@  @@@')
    sleep(0.2)
    print('@@@@@@@@  @@@@ @@@  @@@  @@@  @@@@@@@@       @@@  @@@  @@@  @@@  @@@')
    sleep(0.2)
    print('@@!  @@@  @@!@!@@@  @@!  @@@  @@!  @@@       @@!  @@!  !@@  @@!  !@@')
    sleep(0.2)
    print('!@!  @!@  !@!!@!@!  !@!  @!@  !@!  @!@       !@!  !@!  @!!  !@!  @!!')
    sleep(0.2)
    print('@!@  !@!  @!@ !!@!  @!@  !@!  @!@!!@!        !!@  @!@@!@!   @!@@!@!')
    sleep(0.2)
    print('!@!  !!!  !@!  !!!  !@!  !!!  !!@!@!         !!!  !!@!!!    !!@!!! ')
    sleep(0.2)
    print('!!:  !!!  !!:  !!!  !!:  !!!  !!: :!!        !!:  !!: :!!   !!: :!!')
    sleep(0.2)
    print(':!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  !!:  :!:  :!:  !:!  :!:  !:!')
    sleep(0.2)
    print('::::: ::   ::   ::  ::::: ::  ::   :::  ::: : ::   ::  :::   ::  :::')
    sleep(0.2)
    print(' : :  :   ::    :    : :  :    :   : :   : :::     :   :::   :   :::')
    print(Color.reset)

def menu():
    print(Color.cyan + '--------------------------------------------------------------------')
    print(Color.reset + 'Select options:\n')
    print(Color.yellow + '1) ' + Color.reset + 'Crypt\n' + Color.yellow + '2) ' + Color.reset + 'Decrypt\n' + Color.yellow + '3) ' + Color.reset + 'Quit\n')
    choice = input(Color.yellow + '> ' + Color.reset)
    if not choice.isdecimal():
        system('cls')
        menu()
    else:
        match int(choice):
            case 1: crypt()
            case 2: decrypt()
            case 3: exit()
            case _: menu()

def crypt():
    pass

def decrypt():
    pass

def main():
    title()
    menu()


if __name__ == '__main__':
    main()