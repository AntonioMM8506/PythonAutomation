def isMetro(city):
    if city in ["New York", "Los Angeles", "Chicago"]:
        return True
    else:
        return False
    
print(isMetro("New York"))  # Output: True
print(isMetro("Miami"))     # Output: False