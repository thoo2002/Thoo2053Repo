from dog import Dog
with open("dogs.txt") as file:
    doglist=[]
    for line in file:
        inputs = line.strip()
        tokens = inputs.split()
        newdog=Dog(tokens[0],tokens[1],tokens[2],tokens[3])
        print(newdog)
        doglist.append(newdog)
print(doglist[0].get_name())
print(doglist[0].get_breed())
print(doglist[0].get_trick())
print(doglist[0].isHungry())
print(doglist[0].speak())
doglist[0].feed()
doglist[0].change_trick('fectch')
print(doglist[0].get_name())
print(doglist[0].get_breed())
print(doglist[0].get_trick())
print(doglist[0].isHungry())

