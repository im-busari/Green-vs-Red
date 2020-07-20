import numpy as np

#   Classes
from ZeroGeneration import ZeroGeneration
from NextGeneration import NextGeneration

rows_cols = list(int(num) for num in input("Number of rows, columns: ").split(","))
input_rows = rows_cols[0]
input_columns = rows_cols[1]

#   Creating our Initial Generation
#   Note: Creating "root" object will require to input data, before we proceed
root = ZeroGeneration(input_rows, input_columns)


input_target_n = list(int(num) for num in input("Our target cell [column, row] and number of generations [N]: ").split(","))
target = [input_target_n[0], input_target_n[1]]     # The cell which changes we are going to monitor
number_of_generations = input_target_n[2]
# number_of_generations = int(input("How many generations are we going to have: "))

# Create next_generation object that works with a copy of "Generation Zero"
next_generation = NextGeneration(target, root.zero_generation)

#   Let's produce the required number of generations
next_generation.create_next_generation(number_of_generations)

#   Now we can print-out the result
print(f"The cell was green in {next_generation.green_counter} generations.")
