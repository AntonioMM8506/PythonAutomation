def isMetro(city):
    if city in ["New York", "Los Angeles", "Chicago"]:
        return True
    else:
        return False
    
print(isMetro("New York"))  # Output: True
print(isMetro("Miami"))     # Output: False


def calculateNetIncome(gross_income, state_tax_rate, federal_tax_rate):
    state_tax = gross_income * state_tax_rate
    federal_tax = gross_income * federal_tax_rate
    net_income = gross_income - state_tax - federal_tax
    return net_income
net_income = calculateNetIncome(50000, 0.05, 0.1)
print(f"Net Income: ${net_income:.2f}")  # Output: Net Income: $42500.00
