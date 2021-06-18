import string
import random
import pyperclip
import time

s1 = string.ascii_lowercase
# print(s1)
s2 = string.ascii_uppercase
# print(s2)
s3 = string.digits
 # print(s3)
s4 = string.punctuation
# print(s4)
    
plen = input("Please enter password length: ")
while not(plen.isdigit()):
    print("Please enter correct")
    plen = input("Please enter password length: ")
else:
    plen = int(plen)
    s = []
    s.extend(list(s3))
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    global password
    password = ("".join(s[0:plen]))
    print(f"The generated password is {password}")
    copy = pyperclip.copy(password)
    time.sleep(2)
    print("Password has been copied to your clipboard\nPlease press Ctrl+V to paste.")
    time.sleep(2)
    global account
    account = input("For what account is this password?\n")
    global username
    username = input("Please enter the username for this password\n")
    
    
# print(password)
f = open("passwords.txt", "a+")

f.write(f"\n{account.upper()}username-{username}\n{account.upper()}password-{password}")





f.close()


time.sleep(2)
print("The password has been saved with account name in the text file successfully!")

input("Press enter to close")