#function is a versatile section of reusable code 
#example to display an invoice
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill {amount} is due on {due_date}")

display_invoice("Steve", 101.5, "02-03-2024")
display_invoice("KSI", 221.5, "03-03-2024")

#the position of the argument matters while calling a function, it should match the position in the definition

#return statement
def add(a,b):
    return a+b

print(add(33333,78332)) #returns the addition of the 2 numbers passed

#Default arguments - A default value for certain parameters 
#default is used when the argument is omitted in a function call

def net_price(price, discount = 0, tax_rate = 3.25):
    return price * ((100-discount)/100) * ((100+tax_rate)/100)

print(net_price(500)) #reduces the need to pass arguments unless required or special cases
print(net_price(500,10))
print(net_price(500,tax_rate=6.5))

#it's always a best practice to place the positional paramaters first followed by the default parameter
#positional arguments - use the default order of the arguments mentioned in the funtion definition
#Keyword arguments - argument preceded by an identifier
# used when we need to reference the parameter and overide the original order of arguments
print(net_price(500,tax_rate=6.5))
#another great example of keyword argument is in the print statement
for i in range(1,11):
    print(i, end = " ") #passing a keyword argument to use " " as end character and not \n

print()

#arbitrary arguments
#used when we are unsure how many arguments the user might pass
# *args    : allows user to pass multiple non-key arguments
# **kwargs : allows user to pass multiple keyword-arguments    where * is the unpacking operator

#by default the * operator would unpack the arguments into a tuple which we can iterate over
    
def add(*args):  #will take any number of arguments and pass it as a tuple
    total = 0
    for arg in args:
        total+=arg
    return total

print(add(1,3,44,5,6,7,778,5,8,89))

# ** is used to pack keyword arguments into a dictionary
def print_address(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}: {v}")

print_address(street = "3rd cross", city = "Benga", state = "KARNU", country = "IND")


#when we combine * and ** together, ensure the *args are placed before the **kwargs in the arguments