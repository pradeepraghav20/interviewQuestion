# s="you should Have  have the knowledge of the following"
# s=s.split()
# print(s)
# d={}
# for i in s:
#     d[i]=s.count(i)
#
# print(d)




# rev_s=""
# for i in s:
#     rev_s=i+rev_s
#
# print(rev_s)

s="praadddp"
print(len(s))
rev_s=""
for i in s:
    rev_s=rev_s+i

print(rev_s)
print(len(s))


s="pradeep"
s=list(s)
print(s)
s.reverse()
print("".join(s))