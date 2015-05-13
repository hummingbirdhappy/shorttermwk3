
def state_distribution():
    dictstates = {}
    states = []
    fakecustomers = 'FakeCustomerData.txt'
    infile = open(fakecustomers, 'r')
    customers = infile.readlines()

    for customer in customers[1:]:
        cust_info = customer[1:-1].split(",")
        cust_state = cust_info[7]
        if cust_state not in dictstates:
            dictstates[cust_state] = 1
            states.append(cust_state)
        elif cust_state in dictstates:
            dictstates[cust_state] = dictstates[cust_state] + 1 
            
   
    for state in sorted(dictstates):
        print state, ",", str(dictstates[state])
    return None
    
   

def birth_year_distribution():
    dictyears = {}
    birthyears = []
    fakecustomers = 'FakeCustomerData.txt'
    infile = open(fakecustomers, 'r')
    customers = infile.readlines()

    for customer in customers[1:]:
        cust_info = customer[1:-1].split(",")
        cust_birth = cust_info[13].split("/")
        cust_birthyear = cust_birth[2]
        if cust_birthyear not in dictyears:
            dictyears[cust_birthyear] = 1
            birthyears.append(cust_birthyear)
        elif cust_birthyear in dictyears:
           
            dictyears[cust_birthyear] = dictyears[cust_birthyear] + 1 
            
   
    for year in sorted(dictyears):
        print year, ",", str(dictyears[year])
    return None
     
    


