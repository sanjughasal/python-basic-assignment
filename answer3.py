'''Q3. Uptime Monitoring and Alert System

Write a Python script that checks the uptime of provided URLs and notifies the user if any of the URLs return 4xx or 5xx HTTP status codes (indicating client or server errors). For demonstration purposes, you can use the following URLs as inputs:
4xx (Client Error):
http://www.example.com/nonexistentpage or
http://httpstat.us/404
5xx (Server Error):
http://httpstat.us/500
200 (Successful Response):
https://www.google.com/
Requirements:
URL Check: The script should check the provided URLs and get their HTTP status codes.
Handle Multiple URLs: The script should be able to handle multiple URLs at once, checking each one.
Error Detection: If the status code of any URL is either 4xx or 5xx, the program should:
Notify the user via a print message.
Alternatively, you can implement more advanced logging methods, (log in any log file).
Loop and Monitor: 
You should set up a simple loop that continuously monitors the URLs for a certain interval (e.g., every 10 seconds) to simulate a basic uptime monitoring system.
Status Message: For each URL, the script should output the URL and its current HTTP status code (e.g., 200 OK, 404 Not Found).
'''

import requests
from requests.exceptions import HTTPError
import time

def check_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print(f"{url}: {response.status_code}")

urls = ["http://www.example.com/nonexistentpage",
        "http://httpstat.us/404",
        "http://httpstat.us/500",
        "https://www.google.com/"]

while True:
    for url in urls:
        check_url(url)
    time.sleep(10)  
   
 # Check every 10 seconds
# Output:

# HTTP error occurred: 404 Client Error: Not Found for url: http://www.example.com/nonexistentpage
# HTTP error occurred: 404 Client Error: Not Found for url: http://httpstat.us/404
# HTTP error occurred: 500 Server Error for url: http://httpstat.us/500
# https://www.google.com/: 200
# (The script continuously checks the provided URLs every 10 seconds and prints the HTTP status codes. For URLs returning 4xx or 5xx status codes, it raises an HTTPError and prints the error message. For successful responses (status code 200), it prints the URL and status code.)'''



