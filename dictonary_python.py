info={
    "name" : "Niroj",
    "college" : "Kasthamandap",
    "age": 20
}

print(info)
print(info["age"])

info["name"] = "Saroj"
print(info["name"])

#dictionary methods
print(info.keys()) #print all keys in dictionary
print(info.values()) #print all values in dictionary
print(info.items()) #print all key-value pairs in dictionary
print(info.get("age")) #no error if key is not existed return none

info.update({"city": "kathmandu"}) #add a new key-value pair
print(info)