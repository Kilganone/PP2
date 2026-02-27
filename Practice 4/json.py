import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

x = '{ "name":"Alice", "age":25, "city":"London"}'
y = json.loads(x)
print(y["name"])

x = '{ "product":"Laptop", "price":999, "stock":50}'
y = json.loads(x)
print(y["price"])

x = '{ "active":true, "count":100, "label":"Test"}'
y = json.loads(x)
print(y["active"])

x = '{ "items":["apple", "banana"], "total":2}'
y = json.loads(x)
print(y["items"])

x = {"name": "John", "age": 30, "city": "New York"}
y = json.dumps(x)
print(y)

x = {"product": "Phone", "price": 500}
y = json.dumps(x)
print(y)

x = {"active": True, "verified": False}
y = json.dumps(x)
print(y)

x = {"items": [1, 2, 3], "count": 3}
y = json.dumps(x)
print(y)

x = {"user": None, "id": 123}
y = json.dumps(x)
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))

print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print(json.dumps({"key": "value"}))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

x = {
  "user": "Alice",
  "roles": ["admin", "user"],
  "active": True
}
print(json.dumps(x))

x = {
  "product": "Book",
  "details": {"pages": 200, "author": "Smith"}
}
print(json.dumps(x))

x = {
  "stats": {"wins": 10, "losses": 5},
  "rank": 1
}
print(json.dumps(x))

x = {
  "config": {"theme": "dark", "lang": "en"},
  "version": 2.0
}
print(json.dumps(x))

print(json.dumps(x, indent=4))

x = {"name": "John", "age": 30}
print(json.dumps(x, indent=2))

x = {"product": "Laptop", "price": 999}
print(json.dumps(x, indent=4))

x = {"active": True, "count": 5}
print(json.dumps(x, indent=4))

x = {"items": [1, 2, 3]}
print(json.dumps(x, indent=4))

x = {"name": "John", "age": 30}
print(json.dumps(x, indent=4, separators=(". ", " = ")))

x = {"product": "Phone", "price": 500}
print(json.dumps(x, indent=4, separators=(", ", ": ")))

x = {"active": True, "count": 5}
print(json.dumps(x, indent=2, separators=(". ", " = ")))

x = {"items": [1, 2, 3]}
print(json.dumps(x, indent=2, separators=(", ", ": ")))

x = {"name": "John", "age": 30}
print(json.dumps(x, indent=4, separators=(". ", " = ")))

x = {"name": "John", "age": 30, "city": "New York"}
print(json.dumps(x, indent=4, sort_keys=True))

x = {"product": "Phone", "price": 500, "brand": "X"}
print(json.dumps(x, indent=4, sort_keys=True))

x = {"active": True, "count": 5, "id": 1}
print(json.dumps(x, indent=4, sort_keys=True))

x = {"items": [1, 2, 3], "total": 3}
print(json.dumps(x, indent=4, sort_keys=True))

x = {"name": "John", "age": 30, "city": "New York"}
print(json.dumps(x, indent=4, sort_keys=True))