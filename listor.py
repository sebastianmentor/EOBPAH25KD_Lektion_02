"""
Listor i python (sekvenser)

min_lista1 = []
min_lista2 = [1,2,3,"hejsan", True, 7.23]

"""

min_lista = [1,2,3,4,True,"hejsna", 4.4, []]
print(min_lista)

fyra_första = min_lista[:4]

print(fyra_första)

min_lista2 = min_lista.copy()
min_lista2[0] = "aöslkdöa"

print(id(min_lista))
print(id(min_lista2))

min_lista2[-1].append(23)

print(min_lista)

min_lista.append("Sist i listan")
print(min_lista)

bad_list = min_lista.pop(7)
print(bad_list)
print(min_lista)
print(min_lista2)

bad_list.append("modifierar listan från annan referens")
print(min_lista2)


import copy

min_lista2_copy = copy.deepcopy(min_lista2)
print(id(min_lista2_copy[-1]))
print(id(min_lista2[-1]))


lista_med_listor = [[0]*3]*3
print(lista_med_listor)
lista_med_listor[0][0] = "Hej"
print(lista_med_listor)

# list-metoder
print("********Listmetoder***********")
lst = [1,2]
print(lst)
lst.append(3)
print(lst)
lst.extend([4,5])
print(lst)
lst.extend("hejhej")
print(lst)
lst.insert(1,99)
print(lst)
lst.pop()
print(lst)
lst.pop(0)
print(lst)
lst.remove(99)
print(lst)
print(lst.count("h"))
print(lst.index(5))

lst.clear()
print(lst)

lst = [4,2,3,1,6,5]
print(lst)
lst.sort()
print(lst)

str_list = list("Hejsan hoppsan!")

print(str_list)
str_list.sort()
print(str_list)


for item in str_list:
    print(item)