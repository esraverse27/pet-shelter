import shelter as S
import decorators  

my_shelter = S.Shelter()

print("\n<< my pet shelter >>\n")

while True:
    print("1. add animal")
    print("2. show animals")
    print("3. search animal")
    print("4. add adopter")
    print("5. adopt animal")
    print("6. return animal")
    print("7. Exit shelter")
    task = int(input("what do you want to do?(enter the number): "))
    print("")

    #add animal
    if task == 1:
        try:
            Type = input("what kind of animal do you want?(cat _ dog _ bird _ fish) ")
            if Type not in ["cat" , "dog" , "bird" , "fish"]:
                raise ValueError("not valid input")
        except:
            print("enter a valid type of animal")
            break
        name = input("enter name of animal: ")
        age = input("enter age of animal: ")
        gender = input("mail or femail? ")
        my_shelter.add_animal(Type, name, age, gender)
        print("")

    #show animal
    elif task == 2:
        my_shelter.show_animals()
        print("")

    #finding animal
    elif task == 3:
        name = input("what's the name of animal? ")
        the_animal = my_shelter.find_animal(name)
        print(f"{the_animal.name}({the_animal.age}) _ {the_animal.gender}\n")

    #adding adopter
    elif task == 4:
        @decorators.validate_phone
        def get_phone():
            return input("enter phone number: ")
        @decorators.validate_n_id
        def get_n_id():
            return input("enter national ID: ")

        name = input("enter name of adopter: ")
        phone = get_phone()
        national_id = get_n_id()
        my_shelter.add_adopter(name, phone, national_id)
        print("")

    #adopting animal
    elif task == 5:
        adopter = input("who wants to adopt? ")
        print("which animal wants to adopt? ")
        my_shelter.show_available_animals()
        animal = input("enter the name : ")
        my_shelter.adopt(animal,adopter)
        print("")

    #to return an adopted animal
    elif task == 6:
        pass

    elif task == 7:
        break

    else:
        print("enter a valid choise!")
        continue





