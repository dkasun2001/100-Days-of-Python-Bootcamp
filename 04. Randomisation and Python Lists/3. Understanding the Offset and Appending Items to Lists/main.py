# Lists in Python are defined by square brackets [] and can contain any data type or a mix of data types. 
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[2]) 

# Last item in the list
print(states_of_america[-1]) # Hawaii

print(states_of_america[-2]) # Alaska

# Add an item to the end of the list
states_of_america.append("Kasun")
print(states_of_america)

# Add multiple items to the end of the list
states_of_america.extend(["Dinusha", "Dinusha", "Dinusha"])
print(states_of_america,"\n")

# Insert an item at a specific index
states_of_america.sort( )
print(states_of_america,"\n")

# Sort the list in descending order
states_of_america.sort(reverse=True)
print(states_of_america,"\n")

# Sort the list by the length of the items in the list
states_of_america.sort(key=len)
print(states_of_america,"\n")

# Sort the list by the length of the items in the list in descending order
states_of_america.sort(key=len, reverse=True)
print(states_of_america,"\n")


fruits = ["Apple", "Banana", "Pear", "Peach", "Orange", "Pineapple", "Mango", ]
vegetables = ["Carrot", "Potato", "Onion", "Broccoli", "Cabbage", "Spinach", "Kale", ]

# List of lists
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0][1]) # Banana 