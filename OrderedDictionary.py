from collections import OrderedDict

d = OrderedDict()

d["a"] = 11
d["b"] = 12
d["c"] = 13
d["d"] = 14
d["e"] = 15

print("All the key value pairs:")
for key, value in d.items():
    print(key, value)

print()
print("Filtered key value pairs :")
for key, value in d.items():

    if(key == "a") or value == 12:
        continue
    print(key, value)
