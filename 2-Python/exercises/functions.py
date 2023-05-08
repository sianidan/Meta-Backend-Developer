# Calculate the tax amount added to a customer's bill

def calculateTax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print('Total tax: $', calculateTax(175.00, 15))

print('Total tax: $', calculateTax(164.33, 22))