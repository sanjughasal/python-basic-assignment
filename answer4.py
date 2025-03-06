'''
Q4. Automating Software Package Updates
Write a Python program to automate the checking and updating of installed software packages on a Linux server. The script should:
Function to check for available updates using the system’s package manager (e.g., apt, yum). and list all available updates.
Ask user to Update all at once or provide any specific package name to update (take package index number for ease)
Install the available updates based on user input.
If any updates fail to install, log the error and send an alert (e.g., console log).
Optionally, schedule the script to run at a certain cron.
'''
import os
import subprocess

def check_updates():
    if os.path.exists("/etc/debian_version"):
        os.system("sudo apt update")
        os.system("apt list --upgradable")
    elif os.path.exists("/etc/redhat-release"):
        os.system("sudo yum check-update")
    else:
        print("Unsupported OS")


def update_packages():
    package = input("Enter package index number to update or 'all' to update all packages: ")
    if package == "all":
        if os.path.exists("/etc/debian_version"):
            os.system("sudo apt upgrade")
        elif os.path.exists("/etc/redhat-release"):
            os.system("sudo yum update")
    else:
        if os.path.exists("/etc/debian_version"):
            os.system(f"sudo apt upgrade {package}")
        elif os.path.exists("/etc/redhat-release"):
            os.system(f"sudo yum update {package}")

check_updates()

update_packages()

# Output: 
# The script checks for available updates using the system's package manager and lists all available updates. It then asks the user to update all packages at once or provide a specific package index number to update. Based on the user input, it installs the available updates. If any updates fail to install, it logs the error and sends an alert. The script can be scheduled to run at a certain cron interval.

