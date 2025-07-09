import random
import string

# Tack user to password strength easy, medium and atrong
def tack_strength():
    print('''\n----- Strength -----
1) Easy
2) Medium
3) Strong \n''')
    user_strenghth = input("Choise: ")
    if(user_strenghth.lower() == "easy"):
        return 1
    elif(user_strenghth.lower() == "medium"):
        return 2
    elif(user_strenghth.lower() == "strong"):
        return 3
    else:
        try:
            if(int(user_strenghth) <= 3 and int(user_strenghth) >= 1):
                return int(user_strenghth)
            else:
                print("Enter a number between 1 to 3.\n")
                return 0
        except:
            print("Enter a Valid Input.\n")
            return 0

# check password length
def check_length(length):
    if(length <= 6):
        print("\nPossword is to weak!!!!!!!")
        return 1
    else:
        return tack_strength()

# generat easy password
def easy_password(length):
    upper_password = string.ascii_uppercase
    lower_password = string.ascii_lowercase
    digit_password = string.digits

    passwords = [
        ''.join(random.choice(upper_password) for _ in range(length)), 
        ''.join(random.choice(lower_password) for _ in range(length)), 
        ''.join(random.choice(digit_password) for _ in range(length))
        ]
    return random.choice(passwords)

# for medium level password 
def medium_password(length):
    
    # check the all the characters in lowercase or uppercase and replace onece
    def check_mixletter(mixletter_password):
        used_index = set()
        if not any(i.islower() for i in mixletter_password):
            while True:
                index = random.randint(0, len(mixletter_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.ascii_lowercase)
            mixletter_password = mixletter_password[:index] + addchar + mixletter_password[index+1:]

        elif not any(i.isupper() for i in mixletter_password):
            while True:
                index = random.randint(0, len(mixletter_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.ascii_uppercase)
            mixletter_password = mixletter_password[:index] + addchar + mixletter_password[index+1:]

        return mixletter_password

    # check the all the characters in uppercase or is digits and replace onece
    def check_dwu(dwu_password):
        used_index = set()
        if not any(i.isdigit() for i in dwu_password):
            while True:
                index = random.randint(0, len(dwu_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.digits)
            dwu_password = dwu_password[:index] + addchar + dwu_password[index+1:]

        elif not any(i.isupper() for i in dwu_password):
            while True:
                index = random.randint(0, len(dwu_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.ascii_uppercase)
            dwu_password = dwu_password[:index] + addchar + dwu_password[index+1:]

        return dwu_password

    # check the all the characters in lowercase or is digits and replace onece
    def check_dwl(dwl_password):

        if not any(i.isdigit() for i in dwl_password):
            used_index = set()
            while True:
                index = random.randint(0, len(dwl_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.digits)
            dwl_password = dwl_password[:index] + addchar + dwl_password[index+1:]

        elif not any(i.islower() for i in dwl_password):
            while True:
                index = random.randint(0, len(dwl_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.ascii_lowercase)
            dwl_password = dwl_password[:index] + addchar + dwl_password[index+1:]

        return dwl_password
    
    # generat a meadium lavel password
    mixletter_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(length))
    dwu_password = ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(length))
    dwl_password = ''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(length))
    passwords = [
        check_mixletter(mixletter_password),
        check_dwu(dwu_password),
        check_dwl(dwl_password)
    ]

    return random.choice(passwords)

# for strong Password
def strong_password(length):
    def password_isstrong(strong_password):
        used_index = set()

        if not any(i.isdigit() for i in strong_password):
            while True:
                index = random.randint(0, len(strong_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.digits)
            strong_password = (strong_password[:index] + addchar + strong_password[index+1:])

        if not any(i.isupper() for i in strong_password):
            while True:
                index = random.randint(0, len(strong_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.ascii_uppercase)
            strong_password = (strong_password[:index] + addchar + strong_password[index+1:])

        if not any(i.islower() for i in strong_password):
            while True:
                index = random.randint(0, len(strong_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.ascii_lowercase)
            strong_password = (strong_password[:index] + addchar + strong_password[index+1:])

        if not any(i in string.punctuation for i in strong_password):
            while True:
                index = random.randint(0, len(strong_password) -1)
                if index not in used_index:
                    used_index.add(index)
                    break
            addchar = random.choice(string.punctuation)
            strong_password = (strong_password[:index] + addchar + strong_password[index+1:])

        return strong_password
    
    # generate strong Password
    strong_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password_isstrong(strong_password)

# generate password based on user required
def generate_password(length, strength = 1):
    if(strenghth != 0):
        if(strenghth == 1):
            password = easy_password(length)
        elif(strenghth == 2):
            password = medium_password(length)
        else:
            password = strong_password(length)

        return password
    else:
        return 0

# Main
print("\n----- Simple Password Generator -----")
try:
    length = int(input("Enter password length: "))
    strenghth = check_length(length)
    if(strenghth != 0):
        password = generate_password(length, strenghth)
        print(f"Generated Password: {password}\n")
except ValueError:
    print("Please enter a valid number.\n")
