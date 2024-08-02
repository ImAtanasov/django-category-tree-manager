import requests

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "A", "description": "A", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "B", "description": "B", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "C", "description": "C", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "D", "description": "D", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "E", "description": "E", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "F", "description": "F", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "G", "description": "G", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "H", "description": "H", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# POST request
response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={"name": "I", "description": "I", "parent": None},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)


# Create a similarity between A and B
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "A", "category_b_name": "B"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Create a similarity between A and D
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "A", "category_b_name": "D"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Create a similarity between B and C
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "B", "category_b_name": "C"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Create a similarity between B and D
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "B", "category_b_name": "D"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Create a similarity between C and D
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "C", "category_b_name": "D"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Create a similarity between E and F
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "E", "category_b_name": "F"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Create a similarity between F and G
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "F", "category_b_name": "G"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Create a similarity between F and G
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "F", "category_b_name": "I"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code)
