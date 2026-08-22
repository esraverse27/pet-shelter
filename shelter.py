import animals as an
import adopter as ad 
import my_exc  #this module contains our local exceptions.

class Shelter:
    def __init__(self):
        self.animals_list = []
        self.adopter_list = []


    def add_animal(self, Type , name, age, gender):
        if Type == "cat":
            new_cat = an.cat(name,age,gender)
            self.animals_list.append(new_cat)
            print(f"{new_cat.name} was added.")

        if Type == "dog":
            new_dog = an.dog(name,age,gender)
            self.animals_list.append(new_dog)
            print(f"{new_dog.name} was added.")

        if Type == "bird":
            new_bird = an.bird(name,age,gender)
            self.animals_list.append(new_bird)
            print(f"{new_bird.name} was added.")

        if Type == "fish":
            new_fish = an.fish(name,age,gender)
            self.animals_list.append(new_fish)
            print(f"{new_fish.name} was added.")



    def find_animal(self, name:str):
        try:
            for a in self.animals_list:
                if a.name == name :
                    return a
            else:
                raise my_exc.ListEmptyError("not found")
        except my_exc.ListEmptyError:
            print(f"looks like {a.name} is not here")
            

    def show_animals(self):
        try:
            if self.animals_list:
                for index,a in enumerate(self.animals_list):
                    if a.is_adopted == True:
                        is_adopted = "Unavailable!"
                    else:
                        is_adopted = "Available"
                    print(f"{index+1}. {a.name}({a.age}) _ {is_adopted}")
            else:
                raise my_exc.ListEmptyError("empty")
        except my_exc.ListEmptyError:
            print("nobody is here yet..")


    def show_available_animals(self):
        for index,a in enumerate(self.animals_list):
            if a.is_adopted == False:
                print(f"{index}.{a.name}")



    def add_adopter(self, name:str, phone:str, national_id:str):
        new_adopter = ad.adopter(name, phone, national_id)
        self.adopter_list.append(new_adopter)
        print(f"{new_adopter.name} was successfuly added.")


    def find_adopter(self, name:str):
        try:
            for a in self.adopter_list:
                if a.name == name:
                    return a
            raise ValueError("not found")
        except:
            print("the adopter is not registered.")



    def adopt(self, animal_name:str, adopter_name:str):
        try:
            animal = self.find_animal(animal_name)
            adopter = self.find_adopter(adopter_name)

            if adopter.adopted_animals_count >= 9:
                raise my_exc.AdoptLimitation

            adopter.adopted_animals.append(animal)
            adopter.adopted_animals_count += 1
            animal.is_adopted = True  
            print(f"congratulations a{str(adopter_name)}, you adopted {str(animal_name)}")
            
        except my_exc.AdoptLimitation:
            print("max of adoption is 9")


    def return_adopted_animal(self,animal_name:str, adopter_name:str):
        try:
            animal = self.find_animal(animal_name)
            adopter = self.find_adopter(adopter_name)

            if animal not in adopter.adopted_animals:
                raise my_exc.AddoptionNotVerified

            adopter.adopted_animals_count -= 1
            adopter.adopted_animals.remove(animal)
            animal.is_adopted = False 
            print(f"{animal.name} was returned to shelter.")
        except my_exc.AddoptionNotVerified:
            print(f"{animal.name} does not belong to {adopter.name}.")







        

