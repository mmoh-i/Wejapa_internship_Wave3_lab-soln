#Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = [ ]

# write your for loop here
for i in names:
	#i.lower().replace(' ','_')
	usernames.append(i.lower().replace(' ','_'))

print(usernames)