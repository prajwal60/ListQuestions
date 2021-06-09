# Write a Python program to remove key values pairs from a list of dictionaries.

dict = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]


new_list = [{k:v for k,v in d.items() if k!='key1'} for d in dict]

print(new_list)




# for i in dict:
#     for k,v in i.items():
#         if k!='key1':
#             print("'",k,"'"':',v)
