class Pet:


    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.food_amount = 0

    def eat(self, quantity):
        self.food_amount = self.food_amount - quantity
        if self.food_amount == 0:
            print("Give me more food!")
        else:
            print("Nom Nom Nom...")

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def play(self):
        print("Yipee!")

    def introduce(self):
        print("Hi! My name is " + self.name + "!")

    def feed(self, quantity):
        self.food_amount = self.food_amount + quantity

        if self.food_amount <= 5:
            print("Ooohhh, food!")
        else:
            print("There is too much food! I need to eat some of it!")
    

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Courtney")
pet2 = Pet("Liam")
pet3 = Pet("Nicole")
