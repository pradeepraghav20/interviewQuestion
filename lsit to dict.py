l=[4,4,3,3,5,3]

d={l[i]:l[i+1] for i in range(0,len(l),2)}
print(d)

#reverse dictinoary
from collections import OrderedDict
res=OrderedDict(reversed(list(d.items())))
print(res)


