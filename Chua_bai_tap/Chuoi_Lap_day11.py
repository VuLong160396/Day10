def check(small , big):
    ratio = len(big) // len(small)
    if len(big) % len(small) == 0:
        if small * ratio == big:
            return True
if __name__ == '__main__':
    my_string = input('Input String: ')
    for i in range(1, len(my_string)//2 + 1):
        if check(my_string[None:i], my_string):
            print(f'{my_string} is loop')
            break
    else:
        print(f'{my_string} not loop')













