# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(6)
	example_lines = io.read_example_as_lines(6)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_solution_for(lines, days):
	init_pop = [int(n) for n in lines[0].split(",")]
	population = {n: init_pop.count(n) for n in range(9)}
	for day in range(days):
		new_pop = {}
		for p in range(8, -1, -1):
			if p == 8:
				new_pop[p] = population[0]
			elif p == 6:
				new_pop[p] = population[7] + population[0]
			else:
				new_pop[p] = population[p+1]
		population = new_pop
	return sum(population.values())

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"Simulating the growth rate of lantern fish, how many will exist aft"
       	  f"er 80 days given an intial population?\n")

	results = do_solution_for(example_lines, 80)
	print(f"When we do part one for the example input:")
	print(f"\tThe population size will be {results}")
	print(f"\tWe expected: 5934\n")

	results = do_solution_for(input_lines, 80)
	print(f"When we do part one for the actual input:")
	print(f"\tThe population size will be {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"After 256?\n")

	results = do_solution_for(example_lines, 256)
	print(f"When we do part two for the example input:")
	print(f"\tThe population size will be {results}")
	print(f"\tWe expected: 26984457539\n")

	results = do_solution_for(input_lines, 256)
	print(f"When we do part two for the actual input:")
	print(f"\tThe population size will be {results}\n")

def print_header():
	print("--- DAY 6: Lanternfish ---\n")
