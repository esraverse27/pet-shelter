class animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_adopted = False

        name = str(name)
        gender = str(gender)

    def show_info(self):
        print(f"name: {self.name}\nage: {self.age}\ngender: {self.gender}\nis_adopted: {self.adopted}")

    try:
        def make_sound(self):
            raise NotImplementedError
    except:
        print("the method should be overwrited!")


class cat(animal):
    def __init__(self, name, age , gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        print("I say 'meow'")

class dog(animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        print("I say 'woof'")

class bird(animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        print("I chirp")

class fish(animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        print("I can't make any sound:(")


   





    

    


