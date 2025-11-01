#list is mutable means we can change in it [ ]
# l =[1,2,3] index start from 0
l = [1,2,3,[4,5,6]] #total 4 element 

print(l[3][1])  #5

print(l[0::2])  #[1,3]

print(l[-1::-1])  #reverse the list

p = len(l)

for t in range(p-1,-1,-1):
    print(l[t])

student = ["85","Karan"]

student[0] = "67"

print(student)


print(len(student))

