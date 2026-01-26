import requests
print("Starting httpbin tests...")

print("\n ***  1. BASIC AUTH ***")

url = "https://httpbin.org/basic-auth/galiya/password123"

response = requests.get(
    url,
    auth=("galiya", "password123")
)

print("Request URL:", response.request.url)
print("Status code:", response.status_code)
print("Response JSON:", response.json())


print("\n *** 2. DOWNLOAD IMAGE ***")

image_url = "https://httpbin.org/image/png"
image_response = requests.get(image_url)

print("Request URL:", image_response.request.url)
print("Status code:", image_response.status_code)
print("Content-Type:", image_response.headers.get("Content-Type"))

with open("downloaded_image.png", "wb") as f:
    f.write(image_response.content)

print("Image saved as downloaded_image.png")


print("\n*** 3. GENERATE UUID ***")

uuid_url = "https://httpbin.org/uuid"
uuid_response = requests.get(uuid_url)

print("Request URL:", uuid_response.request.url)
print("Status code:", uuid_response.status_code)
print("Response JSON:", uuid_response.json())


print("\n*** 4. POST JSON ***")

json_url = "https://httpbin.org/post"
payload = {
    "course": "CS162",
    "student": "Galiya",
    "topic": "HTTP requests"
}

json_response = requests.post(json_url, json=payload)

print("Request URL:", json_response.request.url)
print("Status code:", json_response.status_code)
print("Response JSON:", json_response.json())
