# fun with listor i python!

list_with_numbers = [1,2,3,4,5]

summation = 0
for number in list_with_numbers:
    summation += number

print(f"{summation=}")

# "hej" + "då" --> "hejdå"
list_of_things = list_with_numbers + ["Hejsan", "Bannaer", 5.5, True]
print(list_of_things)


list_of_things.append([])

print(list_of_things)

list_of_things.append(list_of_things)

print(list_of_things)

list_of_things[-1].insert(0, "Start")

print(list_of_things)


my_matrix = [[0]*5]*5
# my_matrix = [[0 for n in range(5)] for i in range (5)]
print(my_matrix)

my_matrix[0][0] = 1
my_matrix[1][0] = 4

print(my_matrix)


l = [0,1,2,3,4,5,6,6,6]

for index, i in enumerate(l):
    if i%2 == 0:
        l.pop(index)

print(l)

my_list = ["hej", "då", "igen"]

print(my_list[::-1])

print(list(reversed(my_list)))

# inplace reverse order
my_list.reverse()

print(my_list)

bigger_list = [n for n in range(100)]

print(bigger_list[31:10:-3])

import random

print()
random.shuffle(bigger_list)
print(bigger_list)
# print(bigger_list.sort())
print(sorted(bigger_list))

print(bigger_list)


letters = "abcdEFGhåäöÖÄ"

print(sorted(letters))

####################
import copy

list_one = ["ett", 2, "3", "FYRA", [99]]
list_two = list_one.copy()
list_two = list_one[:]
# list_two = copy.deepcopy(list_one)

list_two[4].append("FEM")

print(f"id of (list_one) = {id(list_one)} and list looks like -->{list_one=}")
print(f"id of (list_two) = {id(list_two)} and list looks like -->{list_two=}")

list_one[4].append(100)

print(f"id of (list_one) = {id(list_one)} and list looks like -->{list_one=}")
print(f"id of (list_two) = {id(list_two)} and list looks like -->{list_two=}")

print(len(list_one))


my_sentence = "Hejsan alla, idag pratar vi bland annat listor! Fun right?"
print(my_sentence.replace("H", "h", count=1))
print(my_sentence.count("n"))

my_s_list = list(my_sentence)
print(my_s_list)
random.shuffle(my_s_list)
print(my_s_list)
my_sentence = "".join(my_s_list)
print(my_sentence)

