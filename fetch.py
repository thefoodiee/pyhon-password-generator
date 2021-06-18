from pprint import pprint
import time
import pyperclip
def process_two_lines(line1: str, line2: str) -> dict:
    # determine which of the 2 variables is the password
    # and which is the username
    if 'password' in line1.split('-')[0]:
        passwordline = line1
        userline = line2
    else:
        passwordline = line2
        userline = line1
    
    # the join is in case the password or username contains a "-" character
    password = '-'.join(passwordline.split('-')[1:]).strip('\n') 
    username = '-'.join(userline.split('-')[1:]).strip('\n')
    service = userline.split('username')[0]
    return {
        'username': username,
        'password': password,
        'service':  service
    }    


def get_login_info(filename: str) -> dict:
    # read file
    with open(filename) as infile:
        filecontents = infile.readlines()
    
    result = []
    # go through lines by pair
    for index, line1 in enumerate(filecontents[::2]):
        result.append(process_two_lines(line1, filecontents[(index*2)+1]))

    return result


time.sleep(2)
logininfo = get_login_info('passwords.txt')
pprint(logininfo)
print('----------\n')
time.sleep(2)
for index, line in enumerate(logininfo):
    print(f'{index:2}: {line["service"]}')

time.sleep(2)
service = int(input('Please select the number of the service for which you want the username/password:\n'))

print(f'Username:\n{logininfo[service]["username"]}\nPassword:\n{logininfo[service]["password"]}\n')

copy = int(input(f"1: Copy Username\n2: Copy Password\n0: To exit\n"))
while True:
    copy = int(input(f"1: Copy Username\n2: Copy Password\n0: To exit\n"))
    if copy == 1:
        tobecopied = (f'{logininfo[service]["username"]}')
        pyperclip.copy(tobecopied)
        continue
    elif copy == 2:
        tobecopied = (f'{logininfo[service]["password"]}')
        pyperclip.copy(tobecopied)
        continue
    else:
        break
