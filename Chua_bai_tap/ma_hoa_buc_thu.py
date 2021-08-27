import random
#choose function code or decode
def function():
    count = 0
    while count < 3:
        code = int(input('Code(1) or Decode(0): '))
        if code in [0,1]:
            return 1 if code == 1 else 0
        else:
            print('Invalid!!!')
        count += 1
#input string and key
def input_string():
    my_string = input('Input string lenght(1-1000): ')
    if len(my_string) > 1000 or len(my_string) < 1:
        print('String Invalid')
    else:
        return my_string
#input key to code
def key():
    k = int(input('Input key < lenght(String): '))
    return k
#__________MAIN__________
if __name__=='__main__':
    choice = function()
    if choice == 1:
        print('Coding.......')
        my_string = input_string()
        print(my_string)
        k = key()
        if int(k) > len(my_string):
            print('Invalid: Key must be smaller than lenght(my_string)!')
        else:
            before = my_string[:k]
            after = my_string[k:None]
            print(f'After Code:{before[::-1]}{after[::-1]}')
    if choice == 0:
        print('Decoding.......')
        my_string = input_string()
        print(my_string)
        k = random.randint(0,len(my_string))
        # if int(k) > len(my_string):
        #     print('Invalid: Key must be smaller than lenght(my_string)!')
        # else:
        before = my_string[:k]
        after = my_string[k:None]
        print(f'After Code:{before[::-1]}{after[::-1]}')