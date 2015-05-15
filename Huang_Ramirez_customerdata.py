'''
File:Huang_Ramirez_customerdata.py
Author:Yinya Huang and Nicol Ramirez
Description:
    Analyzes data from customers to find number of customers in each state and
    number of customers born in each year.
    Receives a text document containing all customer data.
    Returns a list of all states where there are customers, and the number of
    customers in each state.
    Returns a list of all the years in which customers were born, and the number
    of customers born in each year.
'''


def state_distribution():
    '''
    From customer data, creates a dictionary of each state where customers live
    and that state's customer population.
    Receives a text file with all customer data 'FakeCustomerData.txt'
    Returns a dictionary where cust_state is a key and customer population of
    that state is a value.
    Prints each state with its customer population.
    '''
    #create empty dictionary dictstates
    dictstates = {}

    #open FakeCustomerData.txt to read
    fakecustomers = 'FakeCustomerData.txt'
    infile = open(fakecustomers, 'r')

    #creates list called customers where each element is the string of a line
    customers = infile.readlines()

    #for each customer in customers, makes string into list of customer
    #info elements
    for customer in customers[1:]:
        cust_info = customer[1:-1].split(",")

        #assigns name cust_state to 8th element of customer info list 
        cust_state = cust_info[7]

        #adds cust_state to dictstates if not already in dictstates
        #associates value 1 with cust_state
        if cust_state not in dictstates:
            dictstates[cust_state] = 1

        #if cust_state already in dictstates, adds 1 to corresponding value
        else:
            dictstates[cust_state] = dictstates[cust_state] + 1 
            
    #sorts dictionary alphabetically, prints each state with customer population
    for state in sorted(dictstates):
        print state, ",", str(dictstates[state])
    return None
    
   

def birth_year_distribution():
    '''
    From customer data, creates a dictionary of years with number of customers
    born in each year.
    Receives a text file with all customer data 'FakeCustomerData.txt'
    Returns a dictionary where cust_birthyear is a key and number of customers
    born in that year is a value.
    Prints each year with its population of customers born. 
    '''
    #create empty dictionary dictyears
    dictyears = {}

    #open FakeCustomerData.txt to read
    fakecustomers = 'FakeCustomerData.txt'
    infile = open(fakecustomers, 'r')

    #creates list called customers where each element is the string of a line
    customers = infile.readlines()

    #for each customer in customers, makes string into list of customer
    #info elements
    for customer in customers[1:]:
        cust_info = customer[1:-1].split(",")

        #splits 14th element, cust_birth, into 3 parts by "/"
        cust_birth = cust_info[13].split("/")

        #assigns name cust_birthyear to 3rd element of cust_birth
        cust_birthyear = cust_birth[2]

        #adds cust_birthyear to dictyears if not already in dictyears
        #associates value 1 with cust_birthyear      
        if cust_birthyear not in dictyears:
            dictyears[cust_birthyear] = 1

        #if cust_birthyear already in dictyears, adds 1 to corresponding value     
        else:
            dictyears[cust_birthyear] = dictyears[cust_birthyear] + 1 
            
    #sorts dictionary alphabetically, prints each year with number of customers
    #born in that year
    for year in sorted(dictyears):
        print year, ",", str(dictyears[year])
    return None
     
    


