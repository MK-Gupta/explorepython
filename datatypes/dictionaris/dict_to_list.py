



a = {'India':1, 'USA':2}
print(a)

#dictionaris can be printed as list
print(list(a))


print("keys of dict")
print(list(a.keys()))

print("values of the dict")
print(list(a.values()))

#items gives tuples list

print("items of the dict")
print(list(a.items()))


# using the dictionary.items when can use two iteration variables. 


for aa,bb in a.items():
    print(aa,bb)
    print("-------------------")

temp  = list(a.keys())

print("temp", temp)
temp.append("UK")

print("temp new", temp )

