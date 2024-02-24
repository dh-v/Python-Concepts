#creating a dictionary
capitals = {"USA":"Washington",
            "India":"Delhi",
            "Russia":"Moscow",
            "Germany":"Berlin"}

#displaying values using values()
print(capitals.values())
#returns an iterable 
#exact opposite would be keys, i.e print all the keys in a dictionary
print(capitals.keys())

#using get to print values for a defined key
print(capitals.get("USA"))
#a great way to test if a value/key exist is
if capitals.get("Japan"):  #this is beacause get returns none when there is no matching key
    print("Capital exists")
else:
    print("No key exists")

#alternative more common way is 
print(capitals.get("Japan", "Does not exist"))


#using pop() to remove a key:value pair by passing the key as parameter
capitals.pop("USA")
print(capitals)

#using update to add a new pair or update an already existing pair
capitals.update({"Japan":"Tokyo"})
print(capitals)
capitals.update({"USA":"LA"})
print(capitals)


#using set default when we are not sure if a key exists or not, but want to insert it if it doesn't already
capitals.setdefault("Sri Lanka", "Columbo")
print(capitals)

#creating a dictionary from a list 
users = ['Dhv', 'Ayb', 'Brj']
users_dict = dict.fromkeys(users)
print(users_dict)

#to get an iterable for key and value we use
for k, v in capitals.items(): #returns an iterable with keys and values 
    print(k,v)
