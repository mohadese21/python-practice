print("Hello, GitHub!")

moves = ["warm up", "step", "spin"]

for move in moves:
    print("practice:", move)
    
    users = ["mohadese", "ali", "sara"]

for user in users:
    if user=="mohadese":
       print(f"welcome {user}! full access granted.")
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

class DanceSession:

  def __init__(self, style, duration_min): 
     self.style = style
     self.duration_min = duration_min

  def summary(self):
    return f"Style: {self.style} ({self.duration_min} min)"


class SoloRoutine(DanceSession):

  def __init__(self, style, duration_min, bpm):
     super() .__init__(style, duration_min)
     self.bpm = bpm

  def tempo_info(self):
    return f"Tempo: {self.bpm} BPM"

session1 = SoloRoutine("Hip_Hop", 15, 105)
print(session1.summary())
print(session1.tempo_info())
