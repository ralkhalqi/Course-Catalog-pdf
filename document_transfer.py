import requests
import base64
import json
from bs4 import BeautifulSoup 
import wget
import os

def get_catalog(): 
    course_catalog = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')] # Get last catalog 
    return course_catalog

# Download the course catalog from HLS website
course_catalog = get_catalog()
hls_url = "https://hls.harvard.edu/academics/curriculum/catalog/index.html"
hls = requests.get(hls_url)
soup = BeautifulSoup(hls.text, 'html.parser')
links = soup.find_all('a')
for link in links:
    if ('catalog' in link.get('href', []) and '.pdf' in link.get('href', [])):
        response = requests.get(link.get('href'))
        if course_catalog:
            os.remove(course_catalog[0])
        wget.download(link.get('href'))

course_catalog = get_catalog()
if not course_catalog:
    print("Failed to get course catalog link.")

# Authorize user to WP 
username = ""  # ADD THIS
password = ""    # ADD THIS
creds = username + ':' + password
cred_token = base64.b64encode(creds.encode())
header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
url = "" # ADD THIS

# Upload the course catalog to WP
data = open(course_catalog[0], 'rb').read()
response = requests.post(url=url,
                data=data, 
                headers={'Content-Type': '', 'Content-Disposition': 'attachment; filename={}'.format(str(course_catalog[0]))},
                auth=(username, password))
if response.status_code != 200: 
    print("WP User Authorization failed or failed to post media.")
