"""This function takes an argument, a dictionary containing value key pairs of people
   names as the keys and yearly income as values and outputs the yearly tax bill as values"""
def calculate_tax(dict):
    dict = {'Alex': 500, 'James': 20500, 'Kinuthia': 70000}
    print "\nNames and Yearly Incomes"
    print "----------------------------"
    print dict
    #Setting up income ranges
    range0 = range(0,1001)
    range10 = range(1000,10001)
    range15 = range(10000,20201)
    range20 = range(20200,30751)
    range25 = range(30750,50000)

    #initializing tax for each range of income
    tax0=0
    tax10=0
    tax15=0
    tax20=0
    tax25=0

    #calculating the tax applicable for each tax range
    the_range25 = (range25.pop() -range25[0])*0.25
    the_range20 = (range20.pop() -range20[0])*0.20
    the_range15 = (range15.pop() -range15[0])*0.15
    the_range10 = (range10.pop() -range10[0])*0.10
    the_range0 = (range0.pop() -range0[0])*0.0

    #for loop to check the value in key and claculate the tax applicable
    for key, val in dict.items():
        if val in range0:
            first = range0[0]
            valx = val - first
            tax0 = valx * 0.0
            dict0 = tax0
            #print new_dict
            dict[key] = dict0;
        elif val in range10:
            first = range10[0]
            valx = val - first
            tax10 = valx * 0.10
            val10 = tax10 + the_range0
            dict10 = val10
            #print new_dict
            dict[key] = dict10;
        elif val in range15:
            first = range15[0]
            valx = val - first
            tax15 = valx * 0.15
            val15 =  tax15 + the_range10 + the_range0
            dict15 = val15
            #print new_dict
            dict[key] = dict15;
        elif val in range20:
            first = range20[0]
            valx = val - first
            tax20 = valx * 0.20
            val20 =  tax20 + the_range15 + the_range10 + the_range0
            dict20 = val20
            #print new_dict
            dict[key] = dict20;
        elif val in range25:
            first = range25[0]
            valx = val - first
            tax25 = valx * 0.20
            val25 = tax25 + the_range20 + the_range15 + the_range10 + the_range0
            dict25 = val25
            #print new_dict
            dict[key] = dict25;
        elif val > 50000:
            valx = val - 50000
            tax30 = valx * 0.30
            val30 = tax30 + the_range25 + the_range20 + the_range15 + the_range10 + the_range0
            dict30 = val30
            #print new_dict
            dict[key] = dict30;
        else:
            print "Your have a negative yearly income. No tax applicable"
    print "\n\n Names and Yearly Tax Bills"
    print "--------------------------------"
    print dict
    print "\n"

calculate_tax(dict)
