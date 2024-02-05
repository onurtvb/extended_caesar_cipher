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
    phrase = input('Enter the phrase to crypt: ')

    phrase = phrase.upper()

    for x in phrase:
        if x not in CHARACTERS:
            system('cls')
            print(Color.red + 'Error: Invalid Characters' + Color.reset)
            crypt() 

    key = input('Enter the key: ')
    if not key.isdecimal:
        if int(key) < 1:
            system('cls')
            crypt()
        system('cls')
        crypt()
        
    new_phrase = ''
    for x in range(len(phrase)):
        new_phrase += CHARACTERS[CHARACTERS.index(phrase[x])+int(key)]
    print('Crypted phrase:',new_phrase)
    menu()


def decrypt():
    phrase = input('Enter the phrase to decrypt: ')

    phrase = phrase.upper()

    for x in phrase:
        if x not in CHARACTERS:
            system('cls')
            print(Color.red + 'Error: Invalid Characters' + Color.reset)
            crypt() 

    key = input('Enter the key: ')
    if not key.isdecimal:
        if int(key) < 1:
            system('cls')
            crypt()
        system('cls')
        crypt()
        
    new_phrase = ''
    for x in range(len(phrase)):
        new_phrase += CHARACTERS[CHARACTERS.index(phrase[x])-int(key)]
    print('Decrypted phrase:',new_phrase)
    menu()


def main():
    title()
    menu()


if __name__ == '__main__':
    main()