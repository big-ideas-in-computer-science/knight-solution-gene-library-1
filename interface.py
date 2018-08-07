import random 
def create_grid(dimension):
    return [[False for i in range(dimension)]
                for i in range(dimension)
            ]
def check_area(x,y,grid):
    deltas = [
        (2, 1),
        (1, 2),
        (1, -2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (-1, -2),
        (-2, -1),
    ]
    valid = []
    for d in deltas:
        destination = (x + d[0], y + d[1])
        dx = destination[0] -1
        dy = destination[1] -1
        if 0 <= dx and dx < len(grid) and 0 <= dy and dy < len(grid):
            if grid[dx][dy] is False:
                valid.append(destination)
    if len(valid) == 0:
        return None
    else:
        return random.sample(valid, 1)[0]
        
    
class IndividualGene:
    #for the initial position chose a random start position
    def __init__(self, configuration):
        self.configuration = configuration
        self.gene = [(configuration.start_row,configuration.start_col)]
        
    def fill_path(self):
        grid = create_grid(self.configuration.board_size)
        for i in self.gene:
            grid[i[0] -1][i[1] -1] = True
        last_gene = self.gene[len(self.gene)-1]
        while True:
            last_gene = check_area(last_gene[0], last_gene[1],grid)
            if last_gene is None:
                break
            self.gene.append(last_gene)
            grid[last_gene[0] -1][last_gene[1] -1] = True 
        
#mutation is that the line will be maintained until a random postition and randomized on from this point onwards
    def mutate(self):
        splitter = random.randint(1,len(self.gene))
        self.gene = self.gene[0:splitter]
        self.fill_path()
    
#crossover is the product of the replication of one line until the first shared position and replication the second line
    #  from that moment on until the second shared number
    def crossover(self, other):
        self.mutate()
    
#number of steps that follow the rule
    def fitness(self):
        return len(self.gene)
    
#sequence of steps
    def path(self):
        return self.gene


class Configuration:
    def __init__(self, board_size, start_row, start_col, generation_max):
        self.board_size = board_size
        self.start_row = start_row
        self.start_col = start_col
        self.generation_max = generation_max
