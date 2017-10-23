class Logger(object):
  
    def __init__(self, file_name):
        
        self.file_name = file_name
  

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        logger_file = open(self.file_name, "w")
        logger_file.write("The initial conditions for the virus are: \t population size: {} \
            \t vaccination percentage: {} \t virus name: {} \t mortality rate: {}, \
            \t basic reproduction number: {} \n")

    def log_interaction(self, person1, person2, did_infect = None,
                        person2_vacc = None, person2_sick = None):
        
        logger_file = open(self.file_name, "a")

        if did_infect == True and person2_vacc == False:
            person2_sick = True
            logger_file.write("{} did infect {} and {} is now sick. \n".format(person1, person2, person2))
        
        if did_infect == True and person2_vacc == True:
            person2_sick = False
            logger_file.write("{} did not infect {} because {} is vaccinated. \n".format(person1, person2, person2))

        if did_infect == False:
            person2_sick = False
            logger_file.write("{} did not infect {}. \n".format(person1, person2))


    def log_infection_survival(self, person, did_die_from_infection):


        logger_file = open(self.file_name, "a")

        if person.is_alive == False:
            did_die_from_infection = True
            logger_file.write("{} did die from the infection. \n".format(person))

        if person.is_alive == True:
            did_die_from_infection = False
            logger_file.write("{} did not die from the infection. \n".format(person))


    def log_time_step(self, time_step_number):

        logger_file = open(self.file_name, "a")
        logger_file = write("{} is the current time step that has ended. The next step {}. \n".format(time_step_number, time_step_number + 1))

        
