my_dict = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}
for k in my_dict:
    print(f"{k=}")

for v in my_dict.values():
    print(f"{v=}")

# items returns a tuple (key, value) where python understands k=key and v=value
for k, v in my_dict.items():
    print(f"{k=}, {v=}")

# print(my_dict[100])
if 100 in my_dict:
    print(my_dict[100])
else:
    print("value off 100 was not a key in my_dict!")
print(my_dict.get(100, -1))

if {1:2}:
    print("not empty")


a_dict = {"key":"value"}

print(a_dict)
a_dict["myself"] = a_dict
print(a_dict)
a_dict["myself"]["new_key"] = "new_value"
print(a_dict)
