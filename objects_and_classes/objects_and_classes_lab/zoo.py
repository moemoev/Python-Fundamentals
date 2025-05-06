class Zoo:
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            message = f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == 'bird':
            message = f"Birds in {self.name_zoo}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"
        elif species == 'fish':
            message = f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        else:
            message = f"You fucked up, try again!"
        return message


zoo = Zoo(input())
animals = int(input())
for _ in range(animals):
    species, name = input().split()
    zoo.add_animal(species, name)
print(zoo.get_info(input()))


'''
TASK:
Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in the 
zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists 
(mammals, fishes, birds). The class should also have 2 more methods:
add_animal(species, name) - based on the species adds the name to the corresponding list
get_info(species) - based on the species returns a string in the following format: 
"{Species} in {zoo_name}: {names}
Total animals: {total_animals}" 
On the first line you will receive the name of the zoo. On the second line you will receive number n. On the next n 
lines, you will receive animal info in the format: "{species} {name}". Add the animal to the zoo to the corresponding 
list. The "species" command will be mammal, fish, or bird. 
On the final line you will receive a species. At the end, print the info for that species and the total count of animals
in the zoo.
'''