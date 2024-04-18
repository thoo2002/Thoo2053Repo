#Lists
# lst = [10,20,30,40,50]
# lst.append(5)
# lst.append(6)
# lst.append(7)
# print(lst)

# lst.remove(40)
# print(lst)
# lst.pop(2)
# print(lst)

# lst.reverse()
# print(lst)
# lst.sort()
# print(lst)

# lst[0] = 500
# print(lst)

# lst = lst[1:]
# print(lst)

# index7p = lst.index(7)
# print(index7p)

# lst.append(20)
# lst.append(20)
# lst.append(20)
# count20=lst.count(20)
# print(count20)

# lst_copy = lst
# print(lst_copy)
# lst_copy[1] = 99
# print(lst_copy)
# print('original list',lst)

# new_copy=lst.copy()
# print(new_copy)
# new_copy[0]=1000
# print(new_copy)
# print(lst)

# empty_lst = []
# for val in lst:
#     empty_lst.append(val)
# print(empty_lst)

# empty_lst = [0]*10
# print(empty_lst)
# empty_lst[1]=100
# print(empty_lst)

# squares =[]
# for x in range(1,10):
#     squares.append(x*x)
# print(squares)

# lst5 = [x+5 for x in lst]
# print(lst5)

# smallval = [x for x in lst if x <25]
# print(smallval)

#Dictionary
fav_foods = {"Timmy":"Bananas","Ron":"Ice Cream","Tom":"Ice Cream","Sebass":"Steak"}
print(fav_foods)
#To get value of key
print(fav_foods["Timmy"])
#Iterate by keys
for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}")
#Iterate by intems
for person, food in fav_foods.items():
        print(f"{person}'s favorite food is {food}")
#To check if in a dict
if "bob" in fav_foods:
    print(fav_foods['bob'])
else:
    fav_foods['bob'] = 'wings'
print(fav_foods)