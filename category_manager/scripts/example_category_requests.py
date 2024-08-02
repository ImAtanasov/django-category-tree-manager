import requests

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category", "description": "A new category", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 10", "description": "A new category 10", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 11", "description": "A new category 11", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 22", "description": "A new category 22", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 22_1", "description": "A new category 22_1", "parent_name": "New Category 22"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 2", "description": "A new category 2", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3", "description": "A new category 3", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3_1", "description": "A new category 3_1", "parent": 1},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)


response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3_2", "description": "A new category 3_2", "parent_name": "New Category 3"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)


response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3_2_1", "description": "A new category 3_2_1", "parent_name": "New Category 3_2"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)


response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3_2_2", "description": "A new category 3_2_2", "parent_name": "New Category 3_2"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)


response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3_2_3", "description": "A new category 3_2_3", "parent_name": "New Category 3_2"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3_2_4", "description": "A new category 3_2_4", "parent_name": "New Category 3_2"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)


response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "New Category 3_2_5", "description": "A new category 3_2_5", "parent_name": "New Category 3_2"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)


# PUT request
response = requests.put(
    'http://127.0.0.1:8000/api/categories/9/',
    json={"name": "Updated Category", "description": "An updated category", "parent_name": "New Category 3_2"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# PUT request
response = requests.put(
    'http://127.0.0.1:8000/api/updatebyname/New Category 3_2_1/',
    json={"name": "Updated Category 2", "description": "An updated category 2", "parent_name": "New Category 3_2"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# DELETE request
response = requests.delete(
    'http://127.0.0.1:8000/api/deletebyname/Updated Category 2/',
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# DELETE request
response = requests.delete(
    'http://127.0.0.1:8000/api/categories/2/',
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# GET request by name
response = requests.get(
    'http://127.0.0.1:8000/api/getbyname/Updated Category/',
    headers={"Content-Type": "application/json"}
)
print("GET request by name")
print(response.status_code, response.json())

# GET request by parent
response = requests.get(
    'http://127.0.0.1:8000/api/getbyparentname/New Category 22/',
    headers={"Content-Type": "application/json"}
)
print("GET request by parent")
print(response.status_code, response.json())

# GET request all categories
response = requests.get(
    'http://127.0.0.1:8000/api/getallcategories/',
    headers={"Content-Type": "application/json"}
)
print("GET request all categories")
print(response.status_code, response.json())

# GET request by level
response = requests.get(
    'http://127.0.0.1:8000/api/getbylevel/1',
    headers={"Content-Type": "application/json"}
)
print("GET request by level")
print(response.status_code, response.json())
