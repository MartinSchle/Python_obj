class Human:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def set_name(self, new_fname, new_lname):
        self.first_name = new_fname
        self.last_name = new_lname

h = Human("Martin","Schlesinger")
h.set_name("Martina","Schlesingerová")
print(h)

h2 = Human("Karel","Janeček")
print(h2)



it2 = [ 
    Human("Rostislav","Patočka"),
    Human("Šimon","Novák"),
    Human("Matěj","Hajný"),
    Human("Jakub","Pikal")
]
for i in it2:
    print(i)