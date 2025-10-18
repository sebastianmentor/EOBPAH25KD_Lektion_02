"""
En tupel är en oföränderlig ordnad mängd!

t = (4,)

"""

tup = (1,2,3,4) 

print(tup[0])
# tup[0] = 8

print(tup[::-1])

tup2 = (5,6)

ny_tup = tup + tup2
print(ny_tup)
test_tup = (1,2,3,4)
print(tup == test_tup)

single_element_tup = (7,)
print(type(single_element_tup))

my_var = 1,2,3,4

print(my_var)

mix = (1,2,3,"hejsan", True)
print(mix)

big_tup = (1,2,3,4,5,6,7,8,9)

first, *rest, last = big_tup

print(first)
print(rest)
print(last)

point = (4, 7, 9)

x,y,z = point
print(x)
print(y)


for item in big_tup:
    print(f"{item} in big_tup")

point2 = (4, 8)

print(f"{point < point2=}")

