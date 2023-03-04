def sum(datatype, *args):
    if datatype == 'int' :
        s = 0
    elif datatype == 'str':
        s = ''
    for item in args:
        s += item
    return s

print(sum('int',12,34,5))
print(sum('int',12,34,5,67))
print(sum('int',12, 50))
print(sum('str',"ali","reza"))