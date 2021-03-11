monthConversions ={
    "Jan" : "January",
    "Feb" : "Febraury",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
print(monthConversions.get("Luv", " Not a valid key"))

#-------------
customer ={
    "name" : "Vidya shri",
    "age" : 30,
    "is_verified" : True
}

#print(customer["name"])
#print(customer.get("DOB"))
customer["name"] = " Pavani GK"
#print(customer["name"])

#-------------------
phone = input("Phone: ")
digits_mapping = {
     "1" : "One",
     "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

output = ""
for charecters in phone:
    output += digits_mapping.get(charecters, "!") + " "
#print(output)

#----------------Emojis------------------
message = input(">")
words = message.split(' ')
emojis={
      ":)": "\U0001F600",

      ":D": "\U0001F603"
   }

for word in words:
    output += emojis.get(word, word)+ " "
print(output)