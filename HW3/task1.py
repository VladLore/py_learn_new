""""
Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
"""

l1 = [1, 2, 3, 4, 4, 5, 6, 5, 7]
new_lst = []                   
duplicate_lst = []                      

for i in l1:
    if i not in new_lst:
        new_lst.append(i)
    else:
        duplicate_lst.append(i)

print(l1)
print(new_lst)
print(duplicate_lst)