list = []
hi =['hi']
bye = ['bye']
abc = ['abc']
xyz = ['xyz']
list += [(hi, bye)]
#print(list)
list += [(abc, xyz)]
print(list)
print(list[-1])
print(list[-1][-2])
list.pop()
print(list)