# Countdown
def countdown(num):
    arr = []
    for x in range(num, -1, -1):
        arr.append(x)
    return arr
print(countdown(5))

# Print and Return
arr=[]
def print_and_return(list):
        print(list[0])
        return (list[1])
print_and_return([1,2])

#first plus length
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum
print(first_plus_length([1,2,3,4,5]))

#values greater than second
def  values_greater_than_second(list):
    arr = []
    if len(list) < 2:
        return False
    else:
        for x in range(0, len(list)):
            if list[x]>list[1]:
                arr.append(list[x])
    return arr
print(values_greater_than_second([5,2,3,2,1,4]))            

#this length, that value
def  length_and_value(x,y):
    list = []
    for d in range(0,x):
        list.append(y)
    return list
print(length_and_value(6,2))
    
