import urllib.request
import urllib.parse
import json

# Define the base URL for the API
BASE_URL = 'http://localhost:5000/'

# Define the endpoint for retrieving all employees
ENDPOINT = 'employees/'

# Create the full URL by joining the base URL and endpoint
url = urllib.parse.urljoin(BASE_URL, ENDPOINT)

# Send a GET request to retrieve all employees
req = urllib.request.urlopen(url)

# If the request was successful, print out the list of employees
if req.status == 200:
    employees = json.loads(req.read().decode())
    for employee in employees:
        print(f"{employee['first_name']} {employee['last_name']}: {employee['address']['city']}")
else:
    print(f"Error: {req.status} - {req.reason}")
