"""Q2. Write a Python program that generates a password with the following conditions:
At least one uppercase letter.
At least one lowercase letter.
At least two numbers.
At least one special character (e.g., !@#$%&*).
The password should be exactly 16 characters long.
The password should contain no repeating characters.
The password should have a random order each time.
(Do above both problems with Regex and Without Regex)
"""


import random
import string
import re

def generate_password_with_regex():
    while True:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%&*"
        password = "".join(random.sample(chars, 16))
        
        if (re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"\d.*\d", password) and 
            re.search(r"[!@#$%&*]", password)):
            return password

def generate_password_without_regex():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%&*"
    password = [random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.digits),
                random.choice(string.digits),
                random.choice("!@#$%&*")]
    
    while len(password) < 16:
        char = random.choice(chars)
        if char not in password:
            password.append(char)
    
    random.shuffle(password)
    return "".join(password)

print("Password (With Regex):", generate_password_with_regex())
print("Password (Without Regex):", generate_password_without_regex())























'''import random
import string

def generate_password():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%&*"
    password = random.sample(chars, 16)
    return "".join(password)

# Generate password
password = generate_password()
print("Generated Password:", password)
'''