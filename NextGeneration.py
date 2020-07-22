import numpy as np


class NextGeneration:

    def __init__(self, target, previous_generation):
        self.previous_generation = previous_generation
        self.target = target
        self.green_counter = 0

    def generation_builder(self):
        mx_rows = len(self.previous_generation)
        mx_columns = len(self.previous_generation[0])

        new_generation = self.previous_generation.copy()

        # RULES:
        # 1) Each red cell (0) surrounded by 3 or 6 green cells (1) becomes green in the next generation.
        # 2) Each green cell (1) surrounded by 0, 1, 4, 5, 7, 8 green neighbours will become red (0) in the
        #    next generation

        #   Following the rules we will use np.sum on 2D slice of the array that will include all
        #   of the 8 neighbours of our cell. To make sure that the formula will be valid for all elements in the array
        #   I added a border of 0s when I created the array in ZeroGeneration.

        for i in range(1, mx_rows - 1):
            for k in range(1, mx_columns - 1):
                if self.previous_generation[i][k] == 1:
                    num_green_cells = np.sum(self.previous_generation[i - 1:i + 2, k - 1:k + 2]) - 1
                    if num_green_cells in [0, 1, 4, 5, 7, 8]:
                        new_generation[i][k] = 0
                    else:
                        new_generation[i][k] = 1
                elif self.previous_generation[i][k] == 0:
                    num_green_cells = np.sum(self.previous_generation[i - 1:i + 2, k - 1:k + 2])
                    if num_green_cells == 3 or num_green_cells == 6:
                        new_generation[i][k] = 1
                    else:
                        new_generation[i][k] = 0
                else:
                    #   In case we detect a number != 0 or 1, abort task and exit
                    print("We cannot create another generation...")
                    exit()

        return new_generation

    def create_next_generation(self, periods):
        for i in range(periods):
            next_generation = self.generation_builder()
            if next_generation[(self.target[0] + 1), (self.target[1] + 1)] == 1:
                self.green_counter += 1
            # and we make sure to update the previous generation to the new one before we continue
            self.previous_generation = next_generation
