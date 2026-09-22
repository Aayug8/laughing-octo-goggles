my_dict ={}

my_dict ={"name":"aayug","age":11}

print(my_dict["name"])
print(my_dict.get("age"))
my_dict["age"]= 12
print(my_dict)

my_dict["address"] = "downtown"
print(my_dict)
my_dict.pop("age")
print(my_dict)

print("address =", my_dict.get("address"))

my_dict.clear()
print(my_dict)