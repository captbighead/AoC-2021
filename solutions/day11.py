# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(11)
	example_lines = io.read_example_as_lines(11)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_one_for(lines):
	grid = algos.vector_map_from_string_list(lines, lambda: None, int)
	flashes = 0

	for step in range(100):
		
		flashing = set()
		chain = deque()
		for v in grid:
			if grid[v] == None:
				continue
			
			grid[v] += 1

			if grid[v] > 9:
				chain.append(v)

		while chain:
			center = chain.popleft()
			center: vector

			if center in flashing or grid[center] == None:
				continue
			flashing.add(center)

			for v in center.surrounding:
				if grid[v] == None or v in flashing:
					continue
				grid[v] += 1
				if grid[v] > 9:
					chain.append(v)
		
		for v in flashing:
			if grid[v] == None:
				raise LookupError("HOW?")
			grid[v] = 0
			flashes += 1

	return flashes			


def do_part_two_for(lines):
	grid = algos.vector_map_from_string_list(lines, lambda: None, int)
	seeking = True
	step = 0
	goal = len(lines[0]) * len(lines)
	while seeking:
		flashing = set()
		chain = deque()
		for v in grid:
			if grid[v] == None:
				continue
			
			grid[v] += 1

			if grid[v] > 9:
				chain.append(v)

		while chain:
			center = chain.popleft()
			center: vector

			if center in flashing or grid[center] == None:
				continue
			flashing.add(center)

			for v in center.surrounding:
				if grid[v] == None or v in flashing:
					continue
				grid[v] += 1
				if grid[v] > 9:
					chain.append(v)
		
		for v in flashing:
			if grid[v] == None:
				raise LookupError("HOW?")
			grid[v] = 0

		step += 1
		if len(flashing) == goal:
			return step

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"How many times does a dumbo octopus in the input grid flash after 1"
       	  f"00 steps?\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe number of flashes after 100 increments is {results}")
	print(f"\tWe expected: 1656\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe number of flashes after 100 increments is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"How many steps elapse before all the dumbo octopi start flashing in"
       	  f" unison?.\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe number of steps before a simul-flash is {results}")
	print(f"\tWe expected: 195\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe number of steps before a simul-flash is {results}\n")

def print_header():
	print("--- DAY 11: <TITLE GOES HERE> ---\n")
