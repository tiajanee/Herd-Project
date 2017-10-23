import random, sys
random.seed(42)
from person import Person
from logger import Logger

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
        self.logger = logger
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

    def _simulation_should_continue(self): #DONE

        if pop_size == 0 or infected_count == 0:
            return False
        else:
            return True
    

    def run(self):
        # TODO: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0
        # TODO: Remember to set this variable to an intial call of
        # self._simulation_should_continue()!
        should_continue = None
        while should_continue:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.  At the end of each iteration of this loop, remember
        # to rebind should_continue to another call of self._simulation_should_continue()!
            pass
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self): #DONE
        for person.infected in population:
            for i in range(100):
                person in population = random_person
                    if random_person.is_alive = False:
                        break
                    else: 
                        simulation.interaction(person, random_person)
                        interaction.counter += 1
            time_step_counter += 1

    def interaction(self, person, random_person): #DONE
        assert person1.is_alive = True
        assert random_person.is_alive = True

        if random_person.is_vaccinated = True:
            self.logger.log_interaction()
            break

        if random_person.infected = True:
            self.logger.log_interaction()
            break

        if random_person.infected = False and random_person.is_vaccinated = False:
            random_number = random.uniform(0,1)
            if random_number < basic_repro_num:
                newly_infected.append(random_person.ID)
                self.log_interaction()

    def _infect_newly_infected(self): #DONE
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
