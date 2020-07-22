import numpy as np


class ZeroGeneration:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__zero_generation = self.create_zero_generation()

    def create_zero_generation(self):
        zero_list = []
        try:
            for row in range(self.__rows):
                line = list(int(num) for num in input(f"Row {row + 1}: "))

                # verify that we have the correct number of elements
                if len(line) != self.__columns:
                    raise ValueError(f"The number of elements is not equal to the number of columns ({self.__columns})")

                for num in line:
                    if num != 0 and num != 1:
                        raise ValueError(f"You must use only 1s (green) and 0s(red).")

                zero_list.append(line)

            #   Once done we create a 2D NumPy array with border of 0s, that is going to simplify our
            #   code when we produce future generations.
            zero_generation = np.array(zero_list)
            zero_generation = np.pad(zero_generation, pad_width=1, mode='constant', constant_values=0)

            return zero_generation

        except ValueError as err:
            print(f"Unexpected ERROR: {err}")
            print("Please, restart the program.")
            exit()

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
