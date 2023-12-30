# Imports from personal library
from utilities.vector import vector
import utilities.algos as algos
import utilities.io as io

# Imports from standard libraries I find myself using all the time
from collections import defaultdict
from collections import deque

try:
	input_lines = io.read_input_as_lines(9)
	example_lines = io.read_example_as_lines(9)
except:
	input_lines = ["Input Lines Not Found"]
	example_lines = ["Example"]

def do_part_one_for(lines):
	grid = algos.vector_map_from_string_list(lines, default_fn=lambda: 10, 
					  						 interpreter_fn=int)
	lows = []
	for p in list(grid.keys()):
		if all(grid[a] > grid[p] for a in p.adjacents): lows.append(p)
	return sum(1 + grid[p] for p in lows)

def do_part_two_for(lines):
	grid = algos.vector_map_from_string_list(lines, default_fn=lambda: 10, 
					  						 interpreter_fn=int)
	lows = []
	for p in list(grid.keys()):
		if all(grid[a] > grid[p] for a in p.adjacents): lows.append(p)

	basins = []
	for l in lows:
		basin = set([l])
		recent_points = deque([l])
		visited = set()
		while recent_points:
			next_points = deque()
			while recent_points:
				p = recent_points.popleft()
				visited.add(p)
				for a in p.adjacents:
					adpth = grid[a]
					if a not in visited and a not in basin and grid[a] < 9:
						next_points.append(a)
						basin.add(a)
				recent_points = next_points
		basins.append(basin)
	basin_sizes = sorted([len(b) for b in basins], reverse=True)
	return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

def solve_p1():
	print(f"PART ONE\n--------\n")
	print(f"This is the prompt for Part One of the problem.\n")

	results = do_part_one_for(example_lines)
	print(f"When we do part one for the example input:")
	print(f"\tThe number of lowest points (or basins) is {results}")
	print(f"\tWe expected: 15\n")

	results = do_part_one_for(input_lines)
	print(f"When we do part one for the actual input:")
	print(f"\tThe number of lowest points (or basins) is {results}\n")

def solve_p2():
	print(f"PART TWO\n--------\n")
	print(f"This is the prompt for Part Two of the problem.\n")

	results = do_part_two_for(example_lines)
	print(f"When we do part two for the example input:")
	print(f"\tThe product of the three largest basins' sizes is {results}")
	print(f"\tWe expected: 1134\n")

	results = do_part_two_for(input_lines)
	print(f"When we do part two for the actual input:")
	print(f"\tThe product of the three largest basins' sizes is {results}\n")

def print_header():
	print("--- DAY 9: Smoke Basin ---\n")
