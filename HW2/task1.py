def hex_string(num):
    hex_str = hex(num)[2:]
    return '0x' + hex_str

num = int(input('Введите число: '))
hex_str = hex_string(num)
print(hex_str)
print(hex(num))