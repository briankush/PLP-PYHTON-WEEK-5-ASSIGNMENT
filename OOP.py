# Question 1
class TableTennisGame:
    """Base class for table tennis games"""
    def __init__(self, name):
        self.name = name     
    
    def train(self):
        print(f"{self.name} is practicing basic strokes")
    
    def playing(self):
        return "Standard match in progress"

class Duce(TableTennisGame):
    def __init__(self, name):
        super().__init__(name)
        
    def playing(self):  # Polymorphism takes place here
        return f"Deuce in {self.name}! Score tied at 10-10. No winner yet!"

class Win(TableTennisGame):
    def __init__(self, name, winner):
        super().__init__(name)
        self.winner = winner  # Encapsulated through inheritance
    
    def playing(self):  # Polymorphic method
        return f"{self.winner} WINS {self.name}! Final point scored!"

# Match demonstration
matches = [
    Duce("Championship Final"),
    Win("Olympic Semi-Final", "Brian")
]

print("----Table Tennis Match Results ----")
for match in matches:
    print(f"\n {match.playing()}")
    if isinstance(match, Win):
        print(f"Celebration time for {match.winner}!\n")



# Question 2
class Car:
    def move(self):
        print("The car is being driven.....\n")

class Plane:
    def move(self):
        print("The plane is flying.....\n")

class Ship:
    def move(self):
        print("The ship is sailing.....\n")

MeansOfTransport = [Car(), Plane(), Ship(),]


for object in MeansOfTransport:
    object.move()