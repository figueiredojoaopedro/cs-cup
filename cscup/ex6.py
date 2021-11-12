base = input()
num = input()

if base == 'b':
    dec = int(num, 2)
    num = int(num)
    hexa = hex(num).replace('0x','')
    print(f'Decimal = {dec}\nHexadecimal = {hexa[-1]}')
elif base == 'd':
    num = int(num)
    bina = format(num, 'b')
    hexa = format(num, 'X')
    print(f'Binário = {bina}\nHexadecimal = {hexa}')
elif base == 'h':
    dec = int(num, 16)
    bina = str(bin(int(num, 16)))[2:]
    print(f'Binário = {bina}\nDecimal = {dec}')