# Loops
# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1    

# nums=[10,20,30,40,50]
# for i in range(len(nums)):
#     print(nums[i])
# for num in nums:
#     num+=5
#     print(num)
#Loops ex
    # dogs = ["Tofu","Wagyu","Shroom"]
    # for dogn in range(len(dogs)):
    #     print(dogs[dogn])
    # for dogn1 in dogs:
    #     print(dogn1)
    # for i , v in enumerate(dogs):
    #     print(i,v)
#Sum of a list loop
    # nums = [1,2,3,4,5]
    # sum_nums=0
    # for val in nums:
    #     sum_nums += val
    # print("The sum of the nums =",sum_nums)
    # print(f"The sum of the nums = {sum_nums})
#function
# def hello(name="stupid"): # can have a default parameter
#      print("Hello!",name)
# hello()
#strings 
# can us the + to concantenate only other strings with each other not different types of variables
first = "Tim "
last ="Hoo"
fullName = first + last
firstI = first[0]
# can you negative index to go from last to first
last_char = last[-1] # is o
# len still gives length of string
# '*' repeats the string x amount of times
#print(fullName*3)
# equality ==
# not equal !=
# upper make all letter uppercase ex: x.upper()
course = "Platform Computing"
#slicing
platform = course[:8]
computing =course[9:]
#print(platform,computing)
nums=[1, 2, 3, 4, 100]
nums.sort()
XD = nums[1:-1]
lenXD = len(XD)
if lenXD%2 != 0:
    middle = lenXD//2
    XD = XD[middle]
    print (XD)
else:
    XD = sum(XD)/len(XD)
    print(XD)
