l = [1,2,3,"abc"]

n = list(map(lambda x:isinstance(x,str),l))
print(n)