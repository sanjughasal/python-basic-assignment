"""
Q1. Write a Python program to perform the following: 
Validate a given public IP address to check if it follows the correct format (IPv4).
Validate a given email address to check if it’s a valid Gmail address, considering:
It should contain "@gmail.com".
The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.
Provide informative error messages for invalid IP or email.
""" 

def valid_ipv4(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    for i in ip:
        if not i.isdigit():
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True

def valid_gmail(email):
    if email[-10:] != "@gmail.com":
        return False
    username = email.split('@')[0]
    for i in username:
        if not i.isalnum() and i not in ['.', '_']:
            return False
    return True

def valid_input():
    ip = input("Enter IP address: ")
    if valid_ipv4(ip):
        print("Valid IP address")
    else:
        print("Invalid IP address")
    email = input("Enter email address: ")
    if valid_gmail(email):
        print("Valid email address")
    else:
        print("Invalid email address")

valid_input()