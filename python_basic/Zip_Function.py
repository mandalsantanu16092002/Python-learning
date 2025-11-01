l1 = [10,34,5,47,67]
l2 = [22,44,55,99,77,59]

len1 =len(l1)


for h in range(len1):
    print(l1[h],l2[h])


for a, b in zip(l1,l2):
    print(a,b)

