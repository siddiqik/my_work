import requests

BASE_URL = "http://127.0.0.1:5000"

print("== Home ==")
print(requests.get(BASE_URL + "/").text)

print("\n== All students ==")
print(requests.get(BASE_URL + "/students").json())

print("\n== Student with id=2 ==")
print(requests.get(BASE_URL + "/students/2").json())

