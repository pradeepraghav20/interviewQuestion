# s1="abc22"
# s2="a2bc2"
#
#
# if (sorted(s1)==sorted(s2)):
#     print("Yess")
# else:
#     print("Nooo")

s1 = "ythopn"
s2 = "python"
angrame=False
if (len(s1)==len(s2)):
    for i in s1:
        if i in s2:
            if s1.count(i)==s2.count(i):
                angrame=True
            else:
                angrame=False
                break
        else:
            angrame=False

else:
    print("Both string are different")

print(angrame)
