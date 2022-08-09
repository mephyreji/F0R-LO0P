dict ={1:"me",2:"u",3:"he"}
print(dict[1])
print(dict[2])
print(dict[3])
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get(1))
print(dict.get(2))
dict.update({4:"she"})
print(dict)
dict["5"]="I"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()
print(dict)
del dict[2]
print(dict)
dict.clear()
print(dict)
ict ={1:"jain",2:"lan",3:"meln" ,4:"ticn"}
for i in ict.items():
    print(i)
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)
nested_dic={
    "one":
        {
            "name":"john",
            "age":30,
            "city":"newyork"
        },
    "two":
        {
            "name":"bobby"
        }
}
print(nested_dic["two"]["name"])#to extract the a name from

