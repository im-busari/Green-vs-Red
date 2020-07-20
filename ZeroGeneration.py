import numpy as np


class ZeroGeneration:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__zero_generation = self.create_zero_generation()

    def create_zero_generation(self):
        print("[    Enter string of 0s and 1s   ]")
        zero_list = []
        for row in range(self.__rows):
            line = list(int(num) for num in input(f"Row {row + 1}: "))

            # verify that we have the correct number of elements
            if len(line) != self.__columns:
                print(f"""ERROR: The number of elements is not equal to the number of columns ({self._columns}). 
                Please, refresh the program and try again.""")
                exit()

            zero_list.append(line)

        #   Once done we create a 2D NumPy array with border of 0s, that is going to simplify our
        #   code when we produce future generations.
        zero_generation = np.array(zero_list)
        zero_generation = np.pad(zero_generation, pad_width=1, mode='constant', constant_values=0)

        return zero_generation

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    #   Making sure that "Generation Zero" cannot be changed outside this class
    @property
    def zero_generation(self):
        return self.__zero_generation
