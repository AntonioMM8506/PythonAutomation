d = {"k1": {"nestk1": "nestedvalue1", "nestk2": "nestedvalue2"}, "k2": 100, "k3": [1, 2, 3]}
d["k1"]["nestk1"]
d["k1"]["nestk2"]

cars = {
    "bmw": {"model": "550i", "year": 2011, "color": "black"}, 
    "audi": {"model": "a6", "year": 2010, "color": "white"},
    "toyota": {"model": "camry", "year": 2009, "color": "silver"},
    "honda": {"model": "accord", "year": 2008, "color": "blue"},
    "benz": {"model": "c300", "year": 2012, "color": "black"}
}

bmw_year = cars["bmw"]["year"]
audi_year = cars["audi"]["year"]

print(bmw_year)
print(audi_year)
print(cars["toyota"]["model"])
print(cars["honda"]["year"])
print(cars["benz"]["color"])