str = "chicken"

# A String variable can be made upper or lower case given the following methods
str = str.lower()
str = str.upper()
# These commands turn the entire String to upper or lower case and stores it back in str

# The following loop goes through each letter in str one by one. 
# char becomes each letter for each loop!
count = 1
for char in Bob:
    Bob=input("type ")
    if count % 2 == 0 :  # even
        print(char.lower(), end="")
    else:
        print(char.upper(), end="")
    count = count + 1
    