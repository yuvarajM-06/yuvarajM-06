#print a value

print("30 days 30 hour challenge")

print('30 days 30 hour challenge')


#Assigning String to Variable:

Hours = "thirty"
print(Hours)

#Indexing using String:
Days = "Thirty days"
print(Days[0])

#print the particular character from certain text?
Challenge = "I will win"
print(Challenge[7:10])
#Print the length of Character:
Challenge = "I will win"
print(len(Challenge))
#Convert String into lower character;
Challenge = "I will win"
print(Challenge.lower())

#String Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)

#Adding space during concatenation
a = "30 Days"
b = "30 hours"
c = a + " " + b
print(c)

#casefold() - Usage
text = "Thirty days and Thirty hours"

x = text.casefold()
print(x)

x = text.capitalize()
print(x)

x = text.find('e')
print(x)

x = text.isalpha()
print(x)

x = text.isalnum()
print(x)
