#update
thislist = ["apple", "banana", "cherry"]
thislist[1] = 10
print(thislist)  #REPLACE KORCHE

#The insert() method inserts the specified value at the specified position.
#list.insert(pos, elmnt)

l = [7,98,9.9,45,"lio"]

l.insert(4,34)  #INSERT MANE ADD KORCHE
l.pop(5) #delete
print(l)
 
#The append() method appends an element to the end of the list.
#list.append(elmnt) elmnt -> any type (string, number, object etc.)

l.append(24)
print(l)
n = [45,67]
l.append(n)  #exactly jamon ache temon add korbe [] soho
print(l)

l.extend(n)
print(l) #vitor ar elements guloi add korbe


