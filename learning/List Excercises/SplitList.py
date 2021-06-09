# Write a Python program to split a list every Nth element

sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o']
step = 3


def list_slice(sample,step):
    return[sample[i::step]for i in range(step)]


print(list_slice(sample,step))