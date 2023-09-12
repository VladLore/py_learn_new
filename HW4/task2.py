stroka = ''' Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого'''

def uni_code(stroka):
    return sorted([ord(i) for i in set(stroka)], reverse=True)

print(uni_code(stroka))