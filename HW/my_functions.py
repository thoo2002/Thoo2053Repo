#Timothy Hoo
def lst(lst):
    #Returns the third value in a list
    return lst[2]
def Comparitor(input1,input2):
    #Compares the two values and sees which one is bigger
    if(input1 > input2):
        return(f'Input {input1} is greater than {input2}')
    elif(input2 > input1):
        return(f'Input {input2} is greater than {input1}')
    else:
        return(f'Both inputs are equal')
    
#Test of lst
test1 = [1,2,3,4]
print(lst(test1))
test2 = [14,37,22,42,82]
print(lst(test2))
test3 = [27,10,94,38,57]
print(lst(test3))

#Test Comparitor
val1=3
val2=4
#Test when 1>2
print(Comparitor(val1,val2))
#Test when 2>1
print(Comparitor(val2,val1))
#Test when 1==2
print(Comparitor(val1,val1))