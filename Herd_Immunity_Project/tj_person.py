import random

class Person(object):  

    def __init__(self, _id, is_vaccinated, infected=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = None


    def did_survive_infection():

        random_num = random.uniform(0,1)

        if self.infected = None:
            return     
        if self.infected = True and random_num < self.mortality_rate:
            self.is_alive = False

            return False

        if self.infected = True and random_num > self.mortality_rate:
            self.is_alive = True
            self.infected = False

            return True 

            print(self.id, "did survive the infection.")