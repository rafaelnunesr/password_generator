from random import randint

levels = {1: [16, '3 TRILLION YEARS', 128],
          2: [32, '2 QUATTUORDECILLION YEARS', 256],
          3: [64, '6 QUINQUATRIGINTILLION YEARS', 512]}

def generate_password(level):
    password = ''

    while len(password) < levels[level][0]:
        password += chr(randint(33,126))

    return password

def head():
    print('Levels:')
    print('        [1] - 128 bits')
    print('        [2] - 256 bits')
    print('        [3] - 512 bits')

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
            print('YOUR ({} bits) PASSWORD IS: {}{}{}'.format(levels[num][2] , '\033[1;32m', pss, '\033[m'))
            how_much_time_to_break_pwd(num)
        else:
            print('Sorry, Invalid Input')
            main()
    except ValueError:
        print('Sorry, Invalid Input')
        main()

if __name__ == '__main__':
    main()


