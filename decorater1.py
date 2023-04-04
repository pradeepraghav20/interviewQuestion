def grade(fun):
    def grade1(l):
        sum1 = (sum(l)) / len(l)
        if (sum1>6):
            print ("Yess")
        return fun(l)
    return grade1


@grade
def average1(l):
    sum1=(sum(l))/len(l)
    print(sum1)


l=[1,2,3,4,50]
print(average1(l))



s="pradeep"
rev_s=""
for i in s:
    rev_s=i+rev_s


print(rev_s)