class Human():
    def __init__(self):
        print("You are the human who makes world better")
        
class Man(Human):
    def __init__(self, name):
        self.name = name
        print(f"Hello {self.name}. You are the Lucky man")
        
class Woman(Human):
    def __init__(self, name):
        self.name = name
        print(f"Hello {self.name}. You are the lovely woman")


def God():
    #code
    Adam = Man("Adam")
    Eve = Woman("Eve")
    return [Adam, Eve]

#code