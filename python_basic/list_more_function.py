l = [10,20,30,10,25]
a = l.count(10)
print(a)


m = max(l)
print(m)

n = ['hello', 'world']
m = max(n)
print(m)


o = min(l)
print(o)

o = min(n)
print(o)


L = [12,54,23,10,12]
L.sort()  #The sort() method sorts the list ascending by default.
print(L)


#Sort the list descending:
L.sort(reverse=True)
print(L)


cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)


#sort the list by the length of the values:

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)



L.reverse()
print(L)

u = L.index(12)
print(u)

