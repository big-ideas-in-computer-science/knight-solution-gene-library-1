
class IndividualGene:
    #for the initial position chose a random start position
    def __init__(self, configuration):
        self.configuration = configuration
#mutation is that the line will be maintained until a random postition and randomized on from this point onwards
    def mutate(self):
        pass
#crossover is the product of the replication of one line until the first shared position and replication the second line
    #  from that moment on until the second shared number
    def crossover(self, other):
        pass
#number of steps that follow the rule
    def fitness(self):
        pass
#sequence of steps
    def path(self):
        pass


class Configuration:
    def __init__(self, board_size, start_row, start_col, generation_max):
        self.board_size = board_size
        self.start_row = start_row
        self.start_col = start_col
self.generation_max = generation_max
