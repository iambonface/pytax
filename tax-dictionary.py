def calculate_tax(dict):
    dict = {}
    dict = {'Alex': 500, 'James': 20500, 'Kinuthia': 70000}
    tax_range0  = len(range(0,1000)) * 0.00
    tax_range10 = len(range(1000,10000)) * 0.10
    tax_range15 = len(range(10000,20200)) * 0.15
    tax_range20 = len(range(20200,30750)) * 0.20
    tax_range25 = len(range(30750, 50000)) * 0.25

    for key, val in dict.items():
        val = float(val)
        if(val in range(0,1000)):
            tax1 = tax_range0
            dict[key] = tax1
        elif(val in range(1000,10000)):
            r = range(1000,10000)
            val2 = r[0]
            new_val = val - val2
            new_tax = new_val * 0.10
            tax2 = new_tax + tax_range0
            dict[key] = tax2
        elif(val in range(10000,20200)):
            r = range(10000,2020)
            val2 = r[0]
            new_val = val - val2
            new_tax = new_val * 0.15
            tax3 = new_tax + tax_range10 + tax_range0
            dict[key] = tax3
        elif(val in range(20200,30750)):
            r = range(20200,30750)
            val2 = r[0]
            new_val = val - val2
            new_tax = new_val * 0.20
            tax4 = new_tax + tax_range15 + tax_range10 + tax_range0
            dict[key] = tax4
        elif(val in range(30750, 50000)):
            r = range(30750, 50000)
            val2 = r[0]
            new_val = val - val2
            new_tax = new_val * 0.25
            tax5 = new_tax + tax_range20 + tax_range15 + tax_range10 + tax_range0
            dict[key] = tax5
        elif(val > 50000):
            new_val = val - 50000
            new_tax = new_val *0.30
            tax6 = new_tax + tax_range25 + tax_range20 + tax_range15 + tax_range10 + tax_range0
            dict[key] = tax6
        else:
            pass
    print dict
calculate_tax(dict)
