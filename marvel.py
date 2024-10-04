class Character:
    def __init__(self, name, univers, power):
        self.character_name = name
        self.character_univers = univers
        self.character_power = power
    def __str__(self):
        return f"{self.character_name}, {self.character_univers}, {self.character_power}"
    
ch = Character("Thor","Marvel","Mjolnir")
ch2 = Character("Spiderman","Marvel","Cobweb")

print(ch)
print(ch2)