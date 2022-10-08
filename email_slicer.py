# collect email from user
# split the email using the @, save the first part as the username, the second part is gonna be saved as domain 
# split domain using . 

# hello@codewithtomi.com

email = input("Please enter your email: ")

email_split = email.split("@")

username = email_split[0]

domain = email_split[1].split(".")[0]

extension = email_split[1].split(".")[1]

print(f"Username : {username}")
print(f"Domain : {domain}")
print(f"Extension : {extension}")