stroka = ''' Напишите функцию, которая принимает строку текста. Сформируйте список с уникальными кодами Unicode каждого'''

def uni_code(stroka):
    """формирует список используемых символов по убываению"""

    return sorted([ord(i) for i in set(stroka)], reverse=True)

print(uni_code(stroka))