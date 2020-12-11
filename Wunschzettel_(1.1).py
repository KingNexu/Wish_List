__author__ = "KingNexu"
__copyright__ = "Copyright 2020, KingNexu"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "KingNexu"
__email__ = "Py.Nexu@yahoo.com"
__status__ = "Production"


#CODE:

import colorama
from colorama import Fore, Style
import os

colorama.init()


# list menu
def list_menu():
    print(
        'Do you want to ' + Fore.RED + 'create ' + Style.RESET_ALL + 'a new list or to ' + Fore.RED + 'read' + Style.RESET_ALL + ' or to ' + Fore.RED + 'delete' + Style.RESET_ALL + ' a list?')
    print('press ' + Fore.RED + 'q' + Style.RESET_ALL + ' to exit')
    r_or_n = input('>>>')

    if r_or_n == 'create' or r_or_n == '1' or r_or_n == 'c':
        new_list()
    elif r_or_n == 'read' or r_or_n == '2' or r_or_n == 'r':
        read_list()
    elif r_or_n == 'delete' or r_or_n == '3' or r_or_n == 'd':
        delete_list_menu()
    elif r_or_n == 'q' or r_or_n == 'Q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        menu()
    else:
        print(Fore.RED + 'wrong input' + Style.RESET_ALL)
        list_menu()

# create a new list


def new_list():
    print('create mode')
    print('name the list: ')
    a = input('>>>')
    with open(a, 'w') as f:
        print('list successfull created')
        pass

    with open('Listen.txt', 'a') as f:
        all_lists = f.write(a + '\n')
    new_list_redo()

# quit the create


def new_list_redo():
    print(
        'press ' + Fore.RED + 'q' + Style.RESET_ALL + ' to quit or press ' + Fore.RED + 'r' + Style.RESET_ALL + ' to redo the process.')
    d = input('>>>')
    if d == 'q' or d == 'Q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        list_menu()
    elif d == 'r' or d == 'R':
        print(Fore.RED + 'REDO' + Style.RESET_ALL)
        new_list()
    else:
        print(Fore.RED + 'wrong input' + Style.RESET_ALL)
        new_list_redo()

# quit the read


def read_redo():
    print(
        'press ' + Fore.RED + 'q' + Style.RESET_ALL + ' to quit or press ' + Fore.RED + 'r' + Style.RESET_ALL + ' to redo the process.')
    c = input('>>>')
    if c == 'q' or c == 'Q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        list_menu()

    elif c == 'r' or c == 'R':
        print(Fore.RED + 'REDO' + Style.RESET_ALL)
        read_list()
    else:
        print(Fore.RED + 'wrong input' + Style.RESET_ALL)
        read_redo()

# list of witch file to read


def read_list():
    with open('Listen.txt', 'r') as f:
        all_lists = f.read()
    print(all_lists)
    print('exact name of the list: ')
    b = input('>>>')
    try:
        f = open(b, 'r')
        one_list = f.read()
        print(one_list)
    except IOError:
        print(Fore.RED + 'file not accessible' + Style.RESET_ALL)
        read_list()
    finally:
        f.close()
        read_redo()

# menu for delete


def delete_list_menu():
    print(Fore.RED + "'q'" + Fore.WHITE + "to quit" + Style.RESET_ALL)
    with open('Listen.txt', 'r') as f:
        all_lists = f.read()
    print(all_lists)
    print('What list do you want to delete?: ')
    global e
    e = input('>>>')
    if not e == 'q' or e == 'Q':
        try:
            f = open(e, 'r')
            print(f.name)
            print('Are you sure? [y]/[N]')
            g = input('>>>')
            if g == 'y' or g == 'Y' or g == 'Yes':
                os.remove(e)
                delete_list()
                list_menu()
            elif g == 'n' or g == 'Y' or g == 'No':
                print(Fore.RED + 'CANCELLED')
                delete_list_menu()
            else:
                print(Fore.RED + 'wrong input' + Style.RESET_ALL)
                list_menu()
        except IOError:
            print(Fore.RED + 'file not accessible' + Style.RESET_ALL)
            delete_list_menu()
        finally:
            f.close()
    if e == 'q' or e == 'Q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        list_menu()

# delete from Listen.txt


def delete_list():
    with open('Listen.txt', "r") as f:
        lines = f.readlines()
    with open('Listen.txt', "w") as f:
        for line in lines:
            if line.strip("\n") != e:
                f.write(line)


def write_menu():
    print('Which list do you want to write to?')
    with open('Listen.txt', 'r') as f:
        all_lists = f.read()
    print(all_lists)
    print('exact name of the list: ')
    global h
    h = input('>>>')
    if not h == 'q' or h == 'Q':
        try:
            f = open(h, 'r')
            one_list = f.read()
            print(one_list)
            write()
        except IOError:
            print(Fore.RED + 'file not accessible' + Style.RESET_ALL)
            write_menu()
        finally:
            f.close()
    if h == 'q' or h == 'Q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        menu()
    else:
        print(Fore.RED + 'wrong input' + Style.RESET_ALL)
        write_menu()


def write():
    print(Fore.RED + "'q'" + Fore.WHITE + "to quit" + Style.RESET_ALL)
    if h == 'q' or h == 'Q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        write_menu()
    x = input('Wish:')
    if x == 'q' or x == 'q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        write_menu()
    y = input('Link: ')
    if not h == 'q' or h == 'Q':
        with open(h, 'a') as f:
            zettel_schreiben = f.write('[+]' + x + ' -> ' + y + '\n')
    if y == 'q' or y == 'q':
        print(Fore.RED + 'EXIT' + Style.RESET_ALL)
        write_menu()

    write()


def menu():

    print(
        Fore.WHITE + "Tipe" + Fore.RED + "'read'" + Fore.WHITE + "to show all lists to read from \nor  tipe" + Fore.RED + "'write'" + Fore.WHITE + "to add a wish" + Style.RESET_ALL)

    option = input(">>>")

    if option == "read" or option == "1" or option == 'r':
        print("List Menu:")
        list_menu()

    if option == "write" or option == "2" or option == 'w':
        print("Write Menu: ")
        write_menu()


# execution of the programm
menu()
