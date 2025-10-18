"""
dictionarys i python

my_dict = {"key": "value", 3:"person 3", "Sebastian": 99}
my_dict2 = dict(key=value, Sebastian=99) <-- alla keys blir strängar

"""

my_dict = {"key":"value", 8: "number 8"}
my_dict2 = dict(key="value", number8="number 8")

print(my_dict)
print(my_dict2)

print(my_dict["key"])
my_dict["key"] = "new value!"

print(my_dict)
my_dict["new_key"] = 882349
print(my_dict)

for key, value in my_dict.items():
    print(key, "->", value) 


my_dict["lista"] = []
print(my_dict)

my_dict["lista"].append("Hejsan")
print(my_dict)
my_dict["lista"].append(my_dict)
print(my_dict)

personer = {"Kalle": 23, "Lisa":88, "Nisse": 99}

vår_person = personer.get("Sebastian", "Okänd")
print(vår_person)

# personer["Sebastaian"]

sökta_personen = "Sebastian"

if sökta_personen in personer:
    print(f"Värdet för {sökta_personen} är {personer[sökta_personen]}")


del personer["Kalle"]

print(personer)

value_from = personer.pop("Lisa")
print(value_from)
print(personer)

personer.clear()

print(personer)

if not personer:
    print(f"Våran dictionary personer är tom! Kolla {personer}")

personer[88] = "Hejsan"

if personer:
    print(personer)


first_dict = {1: "value 1", 2: "value 2", 3:"value 3"}
second_dict = {3: "another value", 4: "value 4", 5: "number 5"}

second_dict.update(first_dict)
print(second_dict)

# for key, value in second_dict.items():
#     first_dict[key] = value

personer = {"Kalle":
                {"ålder": 33,
                "adress": "hittepå 87",
                "längd":189
                },
            "Lisa":
                {"ålder": 88,
                "adress": "hittepå 23",
                "längd":150
                }

}

print(personer["Lisa"]["längd"])