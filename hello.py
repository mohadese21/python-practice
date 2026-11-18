print("Hello, GitHub!")

moves = ["warm up", "step", "spin"]

for move in moves:
    print("practice:", move)
    
    users = ["mohadese", "ali", "sara"]

for user in users:
    if user=="mohadese":
       print(f"welcome {user}! full access granted.  ")
    else:
        print(f"hello {user}! you are logged in as a guest.")

class User:
    def __init__(self, username, role):
       self.username = username
       self.role = role

user1 = User("mohadese", "admin")
user2 = User("ali", "guest")

print(f"User: {user1.username} | Role:{user1.role}")
print(f"User: {user2.username} | Role: {user2.role}")
