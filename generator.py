from random import randint

levels = {1: [20, '4 SEXTILLION YEARS'], 2: [30, '233 DUODECILLION YEARS'], 3: [40, '15 NOVEMDECILLION YEARS']}

def generate_password(level):
    password = ''

    while len(password) < levels[level][0]:
        password += chr(randint(33,126))

    return password

def head():
    print('Levels:')
    print('        [1] - Low    (20 characteres)')
    print('        [2] - Medium (30 characteres)')
    print('        [3] - Hard   (40 characteres)')

def space():
    for e in range(2):
        print()

def how_much_time_to_break_pwd(level):
    print("It would take {}{}{} to crack your password".format('\033[1;31m', levels[level][1], '\033[m'))

def main():
    head()
    space()
    level = input('Enter a level you want to genenerate the password: ')
    try:
        num = int(level)
        if num > 0 and num < 4:
            pss = generate_password(num)
            print('YOUR PASSWORD IS: {}{}{}'.format('\033[1;32m', pss, '\033[m'))
            how_much_time_to_break_pwd(num)
        else:
            print('Sorry, Invalid Input')
            main()
    except ValueError:
        print('Sorry, Invalid Input')
        main()

if __name__ == '__main__':
    main()


