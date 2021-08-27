N = int(input('Input File(byte): '))
kb = 0
if N <= 4096:
    kb = 4
else:
    big = N // 4096
    small = N % 4096
    # if small == 0:
    #     kb = big * 4
    # else:
    #     kb = (big + 1) * 4
    kb = big * 4 if small == 0 else (big + 1)*4
print(f'Size of File: {kb} KB')