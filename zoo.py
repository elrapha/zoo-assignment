class Zoo:
    def __init__(self,zoo_name,zoo_location,open_hours,zoo_animals_capacity,human_capacity):
        self.zoo_name=zoo_name
        self.zoo_location=zoo_location
        self.working_hours=open_hours
        self.zoo_animals_capacity=zoo_animals_capacity
        self.human_capacity=human_capacity
        self.animals={}
    def add_animal(self,animal,animal_number):
        '''if animal.animal_name in self.animals.keys():
            self.animals[animal.animal_name]+=animal_number
        else:
            self.animals[animal.animal_name]=animal_number'''
        
    def release_animal(self,animal,animal_number):
       ''' if animal_number > 
            if animal.animal_name in self.animals.keys():
                self.animals[animal.animal_name]-=animal_number
            else:
                self.animals[animal.animal_name]=animal_number'''

class Animal(Zoo):
    def __init__(self,animal_name,animal_type,animal_age,pet_name,animal_description):
        Zoo.__init__(self, zoo_name, zoo_location)
        self.animal_name=animal_name
        self.animal_type=animal_type
        self.animal_age=animal_age
        self.pet_name=pet_name
        self.animal_description=animal_description
        
    def make_noise(self):
        print self.description['sound']
    
    def animal_movement(self):
        print self.description['movement']
        
    def perform_trick(self):
        print self.description['trick']
    
    
class Human(Zoo):  
    def __init__(self,human_name,human_age,human_gender,nationality):
        Zoo.__init__(self, zoo_name, zoo_location) open_hours, zoo_animals_capacity, human_capacity)
        
        