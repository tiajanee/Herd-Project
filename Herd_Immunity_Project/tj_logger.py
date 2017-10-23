class Logger(object):
  
    def __init__(self, file_name):
        
        self.file_name = file_name
  

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        file_name = open("herd_log.txt", "w")
        file_name.write("The initial conditions for the virus are: \t population size: {} \
            \t vaccination percentage: {} \t virus name: {} \t mortality rate: {}, \
            \t basic reproduction number: {} \n")

    def log_interaction(self, person1, person2, did_infect = None,
                        person2_vacc = None, person2_sick = None):
        file_name = open("herd_log.txt", "a")

        if did_infect = True and person2_vacc = False:
            person2_sick = True
            file_name.append("{} did infect {} and {} is now sick. \n".format(person1, person2, person2))
        
        if did_infect = True and person2_vacc = True:
            person2_sick = False
            file_name.append("{} did not infect {} because {} is vaccinated. \n".format(person1, person2, person2))

        if did_infect = False:
            person2_sick = False
            file_name.append("{} did not infect {}. \n".format(person1, person2))


    def log_infection_survival(self, person, did_die_from_infection):
    
        file_name = open("herd_log.txt", "a")


        if person.is_alive = False:
            did_die_from_infection = True
            file_name.append("{} did die from the infection. \n".format(person))

        if person.is_alive = True:
            did_die_from_infection = False
            file_name.append("{} did not die from the infection. \n".format(person))


    def log_time_step(self, time_step_number):


        file_name = open("herd_log.txt", "a")
        file_name.append("{} is the current time step. \n".format(time_step_number))

        if time_step_counter > time_step_counter:
            file_name.append("The previous time step has ended. The current time step is {} \n".format(time_step_number))
        

