"""

len()
min()
max()
all()
any()
sorted()

"""

text = "Hejsan 123"
min_lista = [1,2,3,4,5,6,"hejsan", True]
print(len(text))
print(len(min_lista))
# print(len(8))

lista_med_namn = ["Kalle", "Nisse", "Ada", "Sebastian", "Adam", "AAAAAAADDAD"]
lista_med_namn.sort(key=len)
print(lista_med_namn)

tup = (1,2,3,4,5,6)

print(min(tup))
# print(min(min_lista))
print(max(tup))

print("Namnet som är längst", max(lista_med_namn, key=len))
print("Namnet som är kortast", min(lista_med_namn, key=len))

print(f"{all(min_lista)=}")

påhittat_lista = ["", 0, False, 0.0, "Hejsan"]

print(f"{any(påhittat_lista)=}")

fun_dict = {1:89, 2:33, 4:-23}

print(f"{len(fun_dict)=}")
print(f"{max(fun_dict.values())}")

konstig_dict = {"hejsan": None, "då": None, 42: 0}

print(f"{any(konstig_dict.values())}")



t = (1,2,[1,4,2,-1])

t[2].sort()
print(t)

print(sorted(fun_dict.values()))
