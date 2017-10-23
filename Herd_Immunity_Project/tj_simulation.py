import random, sys
random.seed(42)
from tj_person import Person
from tj_logger import Logger

class Simulation(object):
    

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.newly_infected = []


        self.population = self._create_population(initial_infected)
       
    def _create_population(self, initial_infected):
        population = []
        infected_count = 0
        while len(population) != pop_size:
            rando_number = random.random()
            if infected_count !=  initial_infected:
                person = Person(self.next_person_id, False)
                self.next_person_id += 1
                person.is_infected = True
                infected_count += 1


            if rando_number < vacc_percentage:
                person = Person(self.next_person_id, True)
                self.next_person_id += 1


            if rando_number > vacc_percentage:
                person = Person(self.next_person_id, False)
                self.next_person_id += 1
        return population

    def _simulation_should_continue(self): 

        if pop_size == 0 or infected_count == 0:
            return False
        else:
            return True
    

    def run(self):
        time_step_counter = 0
        should_continue = self._simulation_should_continue
        while should_continue:
            self.time_step()
            log_time_step(time_step_counter)
            time_step_counter += 1
            should_continue = self._simulation_should_continue
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self): 
        for person.infected in population:
            for i in range(100):
                for person in population:
                    if person.is_alive == False:
                        return
                    else: 
                        simulation.interaction(person, random_person)
                        interaction.counter += 1
            time_step_counter += 1

    def interaction(self, person, random_person): 
        assert person1.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated == True:
            self.logger.log_interaction()
            return

        if random_person.infected == True:
            self.logger.log_interaction()
            return

        if random_person.infected == False and random_person.is_vaccinated == False:
            random_number = random.uniform(0,1)
            if random_number < basic_repro_num:
                newly_infected.append(random_person.ID)
                self.log_interaction()

    def _infect_newly_infected(self): 
        for person in self.newly_infected:
                for person.id in self.newly_infected:
                    person.infected = True
                    self.logger.log_interaction()
        del self.infected
        self.infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
