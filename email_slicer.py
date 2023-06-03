
email = input("Please enter email address: ")

sliced = email.split("@")

name = sliced[0]
domain = sliced[1]

print(name + " " + domain)
