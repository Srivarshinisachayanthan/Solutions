import random 

how_many_numbers_do_want_to_print = int(input())
starting_range = int(input())
ending_range = int(input())

for i in range(how_many_numbers_do_want_to_print):
    print(random.randint(starting_range, ending_range),",",end="")
