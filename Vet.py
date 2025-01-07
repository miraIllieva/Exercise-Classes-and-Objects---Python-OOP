class Vet:
    animals:list[str] = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: list[str] = []

    def register_animal(self, animal_name: str):
        if(len(Vet.animals) < self.space):
            self.animals.append((animal_name))
            Vet.animals.append(animal_name)
           # Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        else:
            return f"Not enough space"

    def unregister_animal(self, animal_name: str):
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
           # Vet.space += 1
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"
    def info(self):
        return (f"{self.name} has {len(self.animals)} animals."
                f"{self.space - len(Vet.animals)} space left in clinic")
