

# Generate strong passwords for your accounts on different websites 

# importing the random module 
import random

# note that we also  provide spaces at random places between the letters string 
# which will help to create more random & strong passwords

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
integers = "0123456789"
# include rupees symbol(₹) using [Ctrl + Alt + 4]
specialChar = "[]{}()*.:;/_-@#$^&~`!%<>?₹"

comb = lowerCase + upperCase + integers + specialChar

strongPassLen = 21

strongPassword = "".join(random.sample(comb, strongPassLen))
print(strongPassword)