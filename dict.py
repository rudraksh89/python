#dict is a pair of key and values

marks = {
  "rudy" : 100,
  "rai" : 120
}

print(marks["rudy"])

#it is mutable
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"rudy":99})
print(marks.items())

print(marks.get("rakesh")) #if key does not exist then it will get none
print(marks["rakesh"]) #is key does not exists in dic then it will get error

