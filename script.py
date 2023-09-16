class Human:
    def __init__(self, age, name, surname):
        self.age = age;
        self.name = name;
        self.surname = surname;
        
    def __lt__(self, other):
        return self.age < other.age;
    
    def __repr__(self):
        return f"{self.name} {self.surname}, {self.age}";
        
h1 = Human(12, 'Mane', 'Ghudratyan');
h2 = Human(15, 'Arpi', 'Mkrtchyan');
h3 = Human(30, 'Liana', 'Sahakyan');
h4 = Human(22, 'Sahak', 'Tigranyan');
h5 = Human(42, 'Tigran', 'Hovhannisyan');
h6 = Human(27, 'Meline', 'Ghudratyan');
h7 = Human(10, 'Hovhannes', 'Mamikonyan');
h8 = Human(47, 'Mari', 'Ghudratyan');
h9 = Human(23, 'Aram', 'Petrosyan');
h10 = Human(39, 'Armen', 'Papazyan');
h11 = Human(32, 'Rozi', 'Ghudratyan');
h12 = Human(38, 'Leo', 'Muradyan');
h13 = Human(21, 'Samvel', 'Kirakosyan');
h14 = Human(19, 'Bella', 'Arakelyan');
h15 = Human(20, 'Janna', 'Melikyan');

humans = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15];

for i in range(len(humans)):
    for j in range(len(humans) - i - 1):
        if (humans[j + 1] > humans[j]):
            humans[j + 1], humans[j] = humans[j], humans[j + 1];
print('Human:',humans);         
