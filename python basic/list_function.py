#Function for delete Element from list

l = [0,1.5,"hello,89", 90, 2+3j]

#The del keyword is used to delete objects. 
# In Python everything is an object, so the del keyword can also be used to delete 
# variables, lists, or parts of a list etc.
del l[1]
print(l)


#Syntax  --->  list.pop(pos)
v = l.pop(2)
print(l)
print(v)  #Return the removed element DIFFERENCE FROM DEL

l.pop()  #default value is -1, which delete the last item
print(l)


p = [56,90,95,44]

p.remove(90)
print(p)
#p.remove(88) not in the list gives error
#If there are more than one item with the specified value, 
# the remove() method removes the first occurrence


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#clear -> whole list delete

