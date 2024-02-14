class Pet:

    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner = "none"):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.owner = owner
        self.all.append(self)
        pass
    pass

class Owner:


    def __init__(self, name):
        self.name = name
        pass

    def pets(self):
        return [pet for pet in Pet.all]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda x: x.name)

    pass