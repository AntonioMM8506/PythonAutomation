# key: value
# No sequenced, no indexing => Mapping

car = {
    "make" : "bmw",
    "model": "5501",
    "year": 2011
}

print(car)
print(car["make"])
print(car["model"])
print(car["year"])

d = {}
d["one"] = 1
d["two"] = 2
print(d)

sum = d["one"] + d["two"] + 8
print(sum)


d["one"] = 11
d["two"] = 22
print(d)
