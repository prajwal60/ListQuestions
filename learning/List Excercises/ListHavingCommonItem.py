# Write a Python function that takes two lists and returns True if they have at least one common member.

def commonCheck(list1,list2):
    result= False 
    for item1 in list1:
        for item2 in list2:
            if item1==item2:
                result = True
    return result
            

sample1 = [1,2,3,8]
sample2 = [10,12,5,9]

print(commonCheck(sample1,sample2))

