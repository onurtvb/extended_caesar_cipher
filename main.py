from config import CHARACTERS
from colors import Color
from time import sleep


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
    pass

def crypt(phrase:str, key:int):
    pass

def decrypt(phrase:str, key:int):
    pass

def main():
    title()
    menu()


if __name__ == '__main__':
    main()