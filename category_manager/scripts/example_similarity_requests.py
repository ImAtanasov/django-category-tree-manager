import requests


# Create a similarity between Category_A and Category_B
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "New Category 11", "category_b_name": "New Category 10"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code, response.json())

# Create a similarity by category name
response = requests.post(
    'http://127.0.0.1:8000/api/create/',
    json={"category_a_name": "New Category", "category_b_name": "New Category 10"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code, response.json())


# Get the similarity by category name
response = requests.get(
    'http://127.0.0.1:8000/api/getbya/New Category 10/',
    headers={"Content-Type": "application/json"}
)
print(response.status_code, response.json())

# Update the similarity by category name
response = requests.put(
    'http://127.0.0.1:8000/api/updatebya/New Category 10/',
    json={"category_a_name": "New Category 10", "category_b_name": "Updated Category"},
    headers={"Content-Type": "application/json"}
)
print(response.status_code, response.json())

# Delete the similarity by category name
response = requests.delete(
    'http://127.0.0.1:8000/api/deletebya/New Category/',
    headers={"Content-Type": "application/json"}
)
print(response.status_code)

# Get all similarities
response = requests.get(
    'http://127.0.0.1:8000/api/getallsimilarities/',
    headers={"Content-Type": "application/json"}
)
print(response.status_code, response.json())
