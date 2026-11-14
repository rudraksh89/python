#python list are container to store a set of values of any data type 

a = ["Apple",4,3.4,False]

#strings are immutable
#whereas list are mutable

a[0] = "grapes"
print(a)
print(a[0:3])

#methods
a.append("rudy");
b = [3,52,14,56,7]
b.sort()
b.reverse()

a.insert(2,9)
a.pop(1)
a.remove(9)
print(a)
print(b)